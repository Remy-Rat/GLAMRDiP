"""Daily inventory digest — builds 4 per-region Slack posts.

Pipeline:
  1. Run Ops/Scripts/extract.py for each region → JSON in /tmp.
  2. Run this script → prints 4 per-region message strings to stdout (one per
     section, separated by `===== <REGION> =====`).
  3. Caller posts each block to Slack C0AT34JKHL7 via slack_send_message.

Usage:
    # Default — today's date, no qualitative summaries/actions:
    python3 Ops/Scripts/daily_digest.py

    # With qualitative input file (JSON keyed by region name):
    python3 Ops/Scripts/daily_digest.py --qualitative /tmp/qualitative.json

    # Filter out actions that yesterday's posts had threads marking them done
    # and tag carryovers as [ongoing] instead of [new]:
    python3 Ops/Scripts/daily_digest.py \\
      --qualitative /tmp/qualitative.json \\
      --completed /tmp/completed.json \\
      --prior /tmp/prior_actions.json

    # Custom date for backfills:
    python3 Ops/Scripts/daily_digest.py --date 2026-04-20

The qualitative JSON format (one entry per region, list of action strings):
    {
      "AUS": ["Do X", "Do Y"],
      "UK":  ["..."],
      ...
    }

The completed JSON format (one entry per region, list of strings or substrings
of action text that should be suppressed from today's post — typically inferred
by the caller from yesterday's thread replies):
    {
      "AUS": ["Place Heal fill PO with Peter", "Confirm with Jake/Katrina"],
      "UK":  [],
      ...
    }
Matching is case-insensitive substring — keep entries short and distinctive.

The prior-actions JSON format mirrors completed.json — one entry per region
with substrings of yesterday's action text. If today's action matches any, it
renders as [ongoing]; otherwise [new].
    {
      "AUS": ["PO 10 Heal recount", "Heal fill via Outsource"],
      ...
    }
"""
import argparse
import json
from datetime import datetime, date, timedelta

REGIONS = [
    ("AUS", "🇦🇺", "/tmp/digest_aus.json"),
    ("UK", "🇬🇧", "/tmp/digest_uk.json"),
    ("CA", "🇨🇦", "/tmp/digest_ca.json"),
    ("Nordic", "🇳🇴", "/tmp/digest_nordic.json"),
]

PACKAGING_EXACT = {"ACC-INS", "ACC-THA", "ACC-LAB"}
PACKAGING_PREFIXES = ("STO-",)
LOOKBACK_DEDUCTION_DAYS = 3

# Shopify vs DSR anomaly thresholds
OVER_MULTIPLIER = 3.0           # actual >= 3x projected
MIN_PROJECTED_FOR_OVER = 1.0    # avoid noise from tiny projections
DEAD_30D_MIN = 2.0              # was selling >=2/d on 30d window
DEAD_CAP = 3
OVER_CAP = 3

# Slack-rendering constants — see notes at bottom of file.
GAP = "\u200b"            # zero-width space — forces a visible empty paragraph
DIVIDER = "─" * 60        # U+2500 box-drawing horizontal — not parsed as HR


def is_kit(sku):
    return "KIT-" in sku


def is_colour(sku):
    return sku.startswith("POW-")


def is_liquid(sku):
    return sku.startswith("LIQ-") or sku.startswith("ACC-REM")


def is_packaging(sku):
    return sku in PACKAGING_EXACT or sku.startswith(PACKAGING_PREFIXES)


def is_accessory(sku):
    return (
        sku.startswith("ACC-")
        and not sku.startswith("ACC-REM")
        and sku not in PACKAGING_EXACT
    ) or sku.startswith("HEA-")


def classify(sku):
    if is_kit(sku):
        return "kits"
    if is_colour(sku):
        return "colours"
    if is_liquid(sku):
        return "liquids"
    if is_accessory(sku):
        return "accessories"
    return None


def fmt_pct(x):
    if x is None:
        return "n/a"
    sign = "+" if x >= 0 else ""
    return f"{sign}{round(x*100)}%"


def fmt_date_short(iso):
    return datetime.fromisoformat(iso).strftime("%-d %b")


def ordinal(n):
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def friendly_name(sku, products):
    for p in products:
        if p["sku"] == sku:
            return p.get("name", sku)
    return sku


def model_dsr_lookup(products):
    return {p["sku"]: (p.get("model_dsr") or 0) for p in products}


def build_region(region, flag, path, today):
    with open(path) as f:
        d = json.load(f)
    sku_dsr = d["shopify"]["sku_dsr"]
    products = d["pos_model"]["products"]
    red_flags = (d.get("tpl") or {}).get("red_flags", [])

    model = model_dsr_lookup(products)

    groups = {
        "kits": {"actual": 0.0, "projected": 0.0, "label": "Kits"},
        "colours": {"actual": 0.0, "projected": 0.0, "label": "Colours"},
        "liquids": {"actual": 0.0, "projected": 0.0, "label": "Liquids"},
        "accessories": {"actual": 0.0, "projected": 0.0, "label": "Accessories"},
    }

    for sku, dsr in sku_dsr.items():
        g = classify(sku)
        if g is None:
            continue
        groups[g]["actual"] += dsr.get("7d", 0) or 0

    # Projected aggregates: only sellable SKUs (those that exist in Shopify).
    # Excludes warehouse-only components (e.g. HEA-EMP, ACC-RE5-BOT) that have
    # a projected fill rate but no customer-facing sales.
    for p in products:
        sku = p["sku"]
        if sku not in sku_dsr:
            continue
        g = classify(sku)
        if g is None:
            continue
        groups[g]["projected"] += p.get("model_dsr") or 0

    for g in groups.values():
        g["delta"] = ((g["actual"] - g["projected"]) / g["projected"]) if g["projected"] else None

    # Shopify vs DSR
    over_selling, dead = [], []
    for sku, dsr in sku_dsr.items():
        g = classify(sku)
        if g is None:
            continue
        s7 = dsr.get("7d", 0) or 0
        s30 = dsr.get("30d", 0) or 0
        proj = model.get(sku, 0)

        if proj >= MIN_PROJECTED_FOR_OVER and s7 >= proj * OVER_MULTIPLIER:
            over_selling.append({
                "sku": sku, "name": friendly_name(sku, products),
                "s7": s7, "proj": proj, "ratio": s7 / proj,
            })
        if s7 == 0 and s30 >= DEAD_30D_MIN:
            dead.append({
                "sku": sku, "name": friendly_name(sku, products), "s30": s30,
            })

    over_selling.sort(key=lambda x: x["ratio"], reverse=True)
    over_selling = over_selling[:OVER_CAP]
    dead.sort(key=lambda x: x["s30"], reverse=True)
    dead = dead[:DEAD_CAP]

    # Shopify vs 3PL — deduction breaches last 3d
    cutoff = (today - timedelta(days=LOOKBACK_DEDUCTION_DAYS)).isoformat()
    breaches = sorted(
        [r for r in red_flags if r["date"] >= cutoff],
        key=lambda x: x["deduction"], reverse=True,
    )[:3]

    return {
        "region": region, "flag": flag, "groups": groups,
        "over_selling": over_selling, "dead": dead, "breaches": breaches,
    }


def build_region_post(b, today, actions=None, prior_actions=None):
    """Build a self-contained Slack post for one region.

    actions (optional): list of action strings. Each rendered as a bullet.
    prior_actions (optional): list of yesterday's action substrings. Any of
    today's actions containing one of these substrings (case-insensitive) is
    tagged [ongoing]; everything else is tagged [new]. If prior_actions is None
    or empty, no tag is added.
    """
    actions = actions or []
    prior_terms = [p.lower() for p in (prior_actions or []) if p]

    day = ordinal(today.day)
    title = f"{day} {today.strftime('%b %Y')} - DAILY DIGEST"
    header = f"**{title} · {b['flag']} {b['region']}**"

    lines = [DIVIDER, GAP, header, GAP]

    g = b["groups"]["kits"]
    lines.append(
        f"**{g['label']}:** projecting **{round(g['projected'],1)}/d**, "
        f"selling **{round(g['actual'],1)}/d** ({fmt_pct(g['delta'])} vs projection)"
    )

    lines.append(GAP)
    lines.append("**`Shopify vs DSR`**")
    if b["over_selling"] or b["dead"]:
        for o in b["over_selling"]:
            lines.append(
                f"• **{o['sku']} ({o['name']}):** selling **{round(o['s7'],1)}/d** vs projected "
                f"**{round(o['proj'],1)}/d** ({o['ratio']:.1f}x over) - check for spike or store issue."
            )
        for dd in b["dead"]:
            lines.append(
                f"• **{dd['sku']} ({dd['name']}):** **0 sales** in last 7d "
                f"(30d avg {round(dd['s30'],1)}/d) - possible listing/stock issue."
            )
    else:
        lines.append("• None.")

    # True blank breaks out of the bullet list so the next code-styled header
    # isn't indented as a list continuation.
    lines.extend(["", GAP, "**`Shopify vs 3PL`**"])
    if b["breaches"]:
        for br in b["breaches"]:
            ratio = br["deduction"] / br["benchmark"] if br["benchmark"] else 0
            lines.append(
                f"• **{br['sku']}:** {br['deduction']} deducted {fmt_date_short(br['date'])} "
                f"({ratio:.1f}x benchmark of {br['benchmark']})."
            )
    else:
        lines.append("• None.")

    if actions:
        lines.extend(["", GAP, "**`Action Points`**"])
        for a in actions:
            text = a.rstrip(".")
            if prior_terms:
                tag = "`[ongoing]`" if any(t in a.lower() for t in prior_terms) else "`[new]`"
                lines.append(f"• {tag} {text}.")
            else:
                lines.append(f"• {text}.")

    return "\n".join(lines)


def filter_completed_actions(actions_by_region, completed_by_region):
    """Drop actions whose text matches any completed-substring for that region.

    Substring match is case-insensitive. Returns a NEW dict — input not mutated.
    """
    if not completed_by_region:
        return actions_by_region
    out = {}
    for region, actions in actions_by_region.items():
        completed_terms = [t.lower() for t in (completed_by_region.get(region) or [])]
        if not completed_terms or not actions:
            out[region] = actions
            continue
        out[region] = [
            a for a in actions
            if not any(term and term in a.lower() for term in completed_terms)
        ]
    return out


def build_all_posts(today, actions_by_region=None, completed_by_region=None, prior_by_region=None):
    actions_by_region = actions_by_region or {}
    prior_by_region = prior_by_region or {}
    actions_by_region = filter_completed_actions(actions_by_region, completed_by_region)
    blocks = [build_region(r, f, p, today) for r, f, p in REGIONS]
    return [
        (b["region"], build_region_post(
            b, today,
            actions_by_region.get(b["region"]),
            prior_by_region.get(b["region"]),
        ))
        for b in blocks
    ]


def main():
    parser = argparse.ArgumentParser(description="Build daily inventory digest posts.")
    parser.add_argument("--date", type=str, default=None,
                        help="Override today's date (YYYY-MM-DD). Defaults to system today.")
    parser.add_argument("--qualitative", type=str, default=None,
                        help="Path to JSON file with per-region summary+actions.")
    parser.add_argument("--completed", type=str, default=None,
                        help="Path to JSON file with per-region completed-action substrings to suppress.")
    parser.add_argument("--prior", type=str, default=None,
                        help="Path to JSON file with per-region prior-day action substrings. "
                             "Actions matching are tagged [ongoing]; the rest [new].")
    args = parser.parse_args()

    today = date.fromisoformat(args.date) if args.date else date.today()
    actions_by_region = {}
    if args.qualitative:
        with open(args.qualitative) as f:
            actions_by_region = json.load(f)
    completed = {}
    if args.completed:
        with open(args.completed) as f:
            completed = json.load(f)
    prior = {}
    if args.prior:
        with open(args.prior) as f:
            prior = json.load(f)

    for region, post in build_all_posts(today, actions_by_region, completed, prior):
        print(f"===== {region} =====")
        print(post)
        print()


if __name__ == "__main__":
    main()


# --------------------------------------------------------------------------
# Slack rendering notes (learned the hard way during initial design):
#
# - The slack_send_message MCP uses STANDARD markdown, not Slack mrkdwn.
#   Use `**bold**` (not `*single asterisk*` which renders as italic).
# - Em-dashes (—) and the multiplication sign (×) are rejected by the proxy
#   ("Invalid content from server"). Use hyphens and "x" instead.
# - Long runs of plain dashes (`-` * N) are parsed as a markdown horizontal
#   rule and rejected ("invalid_blocks"). Use U+2500 box-drawing instead.
# - Blank lines (`\n\n`) inside a bullet list are treated as list continuation
#   by the parser — the next paragraph gets indented under the list. To exit
#   the list cleanly, append "" then GAP before the next non-list element.
# - Zero-width space (U+200B) on its own line preserves a visible paragraph
#   gap that would otherwise be collapsed. Non-breaking space (U+00A0) is
#   rejected by the proxy.
# --------------------------------------------------------------------------
