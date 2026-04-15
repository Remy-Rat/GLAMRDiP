"""
sales_performance.py — Sales performance analysis (commercial lens).

Usage:
    uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py UK > /tmp/uk.json
    cat /tmp/uk.json | uv run --with pandas python3 Ops/Scripts/sales_performance.py

Reads extracted JSON from stdin. Outputs formatted sales performance tables.
Pure sales lens — no inventory, 3PL, or stock discussion.
"""

import sys
import json


def momentum_label(d7, d14, d30):
    """Classify trend momentum from 3 DSR windows."""
    if d30 == 0:
        return "no data"
    r7_14 = (d7 / d14 - 1) * 100 if d14 > 0 else 0
    r14_30 = (d14 / d30 - 1) * 100 if d30 > 0 else 0
    if abs(r7_14) < 5 and abs(r14_30) < 5:
        return "flat"
    if r7_14 > 0 and r14_30 > 0:
        return "accelerating"
    if r7_14 < 0 and r14_30 < 0:
        return "decelerating"
    if r7_14 < 0 and r14_30 > 0:
        return "peaking"
    if r7_14 > 0 and r14_30 < 0:
        return "recovering"
    return "mixed"


def pct_change(newer, older):
    if older == 0:
        return 0
    return (newer / older - 1) * 100


def main():
    data = json.load(sys.stdin)
    region = data["region"]
    pos = data["pos_model"]
    shop = data["shopify"]

    gf = pos["growth_factor"]
    kit_base = pos["kit_dsr_base"]
    kit_base_total = pos["kit_base_total"]
    kit_scaled_total = pos["kit_scaled_total"]
    products = {p["sku"]: p for p in pos["products"]}
    sku_dsr = shop["sku_dsr"]

    # ---- Helpers ----
    def get(sku):
        return sku_dsr.get(sku, {"7d": 0, "14d": 0, "30d": 0})

    # ================================================================
    # GROWTH HEADLINE
    # ================================================================
    kit_skus = ["KIT-STA-2", "KIT-COM-4", "KIT-ULT-6"]
    kit7 = sum(get(s)["7d"] for s in kit_skus)
    kit14 = sum(get(s)["14d"] for s in kit_skus)
    kit30 = sum(get(s)["30d"] for s in kit_skus)
    actual_gf = kit14 / kit_base_total if kit_base_total else 0
    vs_target = pct_change(kit14, kit_scaled_total)
    mom = momentum_label(kit7, kit14, kit30)
    mom7 = pct_change(kit7, kit30)

    print(f"SALES PERFORMANCE — {region} — {data['extracted_at']}")
    print(f"Shopify latest: {shop['latest_date']}")
    print()
    print("=" * 65)
    print("GROWTH HEADLINE")
    print("=" * 65)
    print(f"  Kit total:     7d={kit7:.1f}  |  14d={kit14:.1f}  |  30d={kit30:.1f}")
    print(f"  Growth factor: {gf}x (model) | {actual_gf:.2f}x (actual) | vs target: {vs_target:+.1f}%")
    print(f"  Momentum:      {mom} ({mom7:+.0f}% 7d vs 30d)")

    # ================================================================
    # CATEGORY PERFORMANCE
    # ================================================================
    print()
    print("=" * 65)
    print("CATEGORY PERFORMANCE")
    print("=" * 65)

    # -- Kits --
    print()
    print("--- KITS ---")
    print(f"{'SKU':15s} {'7d':>7s} {'14d':>7s} {'30d':>7s} {'% total':>8s} {'7d vs 30d':>10s}")
    for sku in kit_skus:
        d = get(sku)
        pct_total = d["14d"] / kit14 * 100 if kit14 > 0 else 0
        chg = pct_change(d["7d"], d["30d"])
        flag = " *" if abs(chg) > 20 else ""
        print(f"{sku:15s} {d['7d']:>7.1f} {d['14d']:>7.1f} {d['30d']:>7.1f} {pct_total:>7.0f}% {chg:>+9.0f}%{flag}")
    print(f"{'TOTAL':15s} {kit7:>7.1f} {kit14:>7.1f} {kit30:>7.1f}")

    # -- Liquids (standalone repurchase signal) --
    liquid_skus = ["LIQ-BAS-2", "LIQ-SEN-2", "LIQ-SEA-3", "LIQ-GLO-4", "LIQ-SEN-4",
                   "LIQ-BON-1", "LIQ-HEA-5", "LIQ-MAT-4", "LIQ-SOA-6"]
    # Filter to only SKUs that exist in Shopify data
    liquid_skus = [s for s in liquid_skus if s in sku_dsr]
    liq7 = sum(get(s)["7d"] for s in liquid_skus)
    liq14 = sum(get(s)["14d"] for s in liquid_skus)
    liq30 = sum(get(s)["30d"] for s in liquid_skus)
    liq_ratio_14 = liq14 / kit14 if kit14 > 0 else 0
    liq_ratio_30 = liq30 / kit30 if kit30 > 0 else 0

    print()
    print("--- LIQUIDS (standalone — repurchase signal) ---")
    print(f"{'SKU':15s} {'7d':>7s} {'14d':>7s} {'30d':>7s} {'7d vs 30d':>10s}")
    for sku in liquid_skus:
        d = get(sku)
        if d["7d"] == 0 and d["14d"] == 0 and d["30d"] == 0:
            continue
        chg = pct_change(d["7d"], d["30d"])
        flag = " *" if abs(chg) > 30 else ""
        print(f"{sku:15s} {d['7d']:>7.1f} {d['14d']:>7.1f} {d['30d']:>7.1f} {chg:>+9.0f}%{flag}")
    print(f"{'TOTAL':15s} {liq7:>7.1f} {liq14:>7.1f} {liq30:>7.1f}")
    print(f"  Liquid-to-kit ratio: {liq_ratio_14:.2f} (14d) | {liq_ratio_30:.2f} (30d)")

    # -- Accessories --
    acc_remove = ["ACC-REM", "ACC-REM-500", "ACC-REM-BOW"]
    acc_bundles = ["ACC-REM-BUN-1", "ACC-REM-BUN-2", "LIQ-SET"]
    acc_other = ["ACC-MAN", "ACC-NAI-SET", "ACC-NAI-100/180", "ACC-NAI-240",
                 "ACC-CUT-PRE", "ACC-BRU", "ACC-PRO-DRI", "ACC-JAR",
                 "ACC-NAI-WIP", "ACC-NAI-MAT", "ACC-NAI-LIN",
                 "ACC-5PC-BAG", "ACC-BOX", "ACC-BAL-BIT"]
    # Filter to existing SKUs
    acc_remove = [s for s in acc_remove if s in sku_dsr]
    acc_bundles = [s for s in acc_bundles if s in sku_dsr]
    acc_other = [s for s in acc_other if s in sku_dsr and (get(s)["14d"] > 0 or get(s)["7d"] > 0)]

    print()
    print("--- ACCESSORIES ---")
    print(f"{'SKU':20s} {'7d':>7s} {'14d':>7s} {'30d':>7s} {'7d vs 30d':>10s}")
    for sku in acc_remove + acc_bundles + acc_other:
        d = get(sku)
        if d["7d"] == 0 and d["14d"] == 0 and d["30d"] == 0:
            continue
        chg = pct_change(d["7d"], d["30d"])
        flag = " *" if abs(chg) > 30 else ""
        label = ""
        if sku in acc_bundles:
            label = " (bundle)"
        print(f"{sku:20s} {d['7d']:>7.1f} {d['14d']:>7.1f} {d['30d']:>7.1f} {chg:>+9.0f}%{flag}{label}")

    # -- Colours --
    colour_data = [(sku, d) for sku, d in sku_dsr.items() if sku.startswith("POW-")]
    total_c7 = sum(d["7d"] for _, d in colour_data)
    total_c14 = sum(d["14d"] for _, d in colour_data)
    total_c30 = sum(d["30d"] for _, d in colour_data)
    active_gt5 = sum(1 for _, d in colour_data if d["14d"] > 5)
    active_gt2 = sum(1 for _, d in colour_data if d["14d"] > 2)
    active_gt1 = sum(1 for _, d in colour_data if d["14d"] > 1)
    active_gt0 = sum(1 for _, d in colour_data if d["14d"] > 0)
    active_zero = sum(1 for _, d in colour_data if d["14d"] == 0)
    c_per_kit = total_c14 / kit14 if kit14 > 0 else 0

    # Expected colours per kit based on mix
    sta_pct = get("KIT-STA-2")["14d"] / kit14 if kit14 > 0 else 0
    com_pct = get("KIT-COM-4")["14d"] / kit14 if kit14 > 0 else 0
    ult_pct = get("KIT-ULT-6")["14d"] / kit14 if kit14 > 0 else 0
    expected_c_per_kit = sta_pct * 3 + com_pct * 6 + ult_pct * 9

    print()
    print("--- COLOURS (summary) ---")
    print(f"  Total: 7d={total_c7:.0f} | 14d={total_c14:.0f} | 30d={total_c30:.0f}")
    print(f"  Colours per kit: {c_per_kit:.1f} (expected from mix: {expected_c_per_kit:.1f})")
    delta = c_per_kit - expected_c_per_kit
    if abs(delta) > 0.5:
        direction = "above" if delta > 0 else "below"
        print(f"  {abs(delta):.1f} {direction} expected — {'standalone colour sales adding volume' if delta > 0 else 'some kit orders not picking full allocation?'}")
    print(f"  Active: {active_gt5} (>5/d) | {active_gt2} (>2/d) | {active_gt1} (>1/d) | {active_gt0} (>0/d) | {active_zero} (zero)")

    # ================================================================
    # WEEKLY KIT TREND
    # ================================================================
    print()
    print("=" * 65)
    print("WEEKLY KIT TREND")
    print("=" * 65)
    weeks = shop["weekly_kit_trend"]
    # Compute rolling 4-week avg
    rates = [w["daily_rate"] for w in weeks]
    print(f"{'Week':>6s} {'Dates':>22s} {'Days':>5s} {'Total':>7s} {'Daily':>7s} {'vs Model':>9s} {'WoW':>7s} {'4wk Avg':>8s}")
    for i, w in enumerate(weeks):
        vs = pct_change(w["daily_rate"], kit_scaled_total)
        wow = pct_change(w["daily_rate"], weeks[i - 1]["daily_rate"]) if i > 0 else 0
        avg4 = sum(rates[max(0, i - 3):i + 1]) / min(4, i + 1)
        wow_str = f"{wow:+.0f}%" if i > 0 else "—"
        print(f"W{w['week']:>4d} {w['dates']:>22s} {w['days']:>5d} {w['total']:>7d} {w['daily_rate']:>7.1f} {vs:>+8.1f}% {wow_str:>7s} {avg4:>8.1f}")

    # Flags
    flags = []
    for i in range(2, len(weeks)):
        if rates[i] < rates[i - 1] < rates[i - 2]:
            if i == len(weeks) - 1 or (i < len(weeks) - 1 and rates[min(i + 1, len(weeks) - 1)] < rates[i]):
                flags.append("3+ consecutive declining weeks detected")
                break
    for i, w in enumerate(weeks):
        if i >= 4:
            prior = rates[i - 4:i]
            avg_prior = sum(prior) / len(prior)
            if avg_prior > 0 and pct_change(w["daily_rate"], avg_prior) > 30:
                flags.append(f"W{w['week']} spike: {pct_change(w['daily_rate'], avg_prior):+.0f}% above prior 4-week avg (likely promo)")
    if flags:
        print()
        for f in flags:
            print(f"  FLAG: {f}")

    # ================================================================
    # KIT MIX ANALYSIS
    # ================================================================
    print()
    print("=" * 65)
    print("KIT MIX ANALYSIS")
    print("=" * 65)
    print(f"{'Kit':15s} {'14d DSR':>8s} {'14d %':>7s} {'30d DSR':>8s} {'30d %':>7s} {'Model %':>8s} {'Shift':>7s}")
    for sku, label in [("KIT-STA-2", "Starter"), ("KIT-COM-4", "Complete"), ("KIT-ULT-6", "Ultimate")]:
        d = get(sku)
        pct14 = d["14d"] / kit14 * 100 if kit14 > 0 else 0
        pct30 = d["30d"] / kit30 * 100 if kit30 > 0 else 0
        model_pct = kit_base.get(sku, 0) / kit_base_total * 100 if kit_base_total > 0 else 0
        shift = pct14 - pct30
        arrow = "+" if shift > 1 else ("-" if shift < -1 else "=")
        print(f"{label:15s} {d['14d']:>8.1f} {pct14:>6.0f}% {d['30d']:>8.1f} {pct30:>6.0f}% {model_pct:>7.0f}% {arrow}{abs(shift):>5.1f}pp")

    # AOV proxy
    ult_share_14 = get("KIT-ULT-6")["14d"] / kit14 * 100 if kit14 > 0 else 0
    ult_share_30 = get("KIT-ULT-6")["30d"] / kit30 * 100 if kit30 > 0 else 0
    aov_direction = "increasing" if ult_share_14 > ult_share_30 + 1 else ("decreasing" if ult_share_14 < ult_share_30 - 1 else "stable")
    print(f"\n  AOV proxy (ULT share): {ult_share_14:.0f}% (14d) vs {ult_share_30:.0f}% (30d) — {aov_direction}")

    # ================================================================
    # COLOUR INTELLIGENCE
    # ================================================================
    print()
    print("=" * 65)
    print("COLOUR INTELLIGENCE")
    print("=" * 65)

    # Top 10 by volume
    by_vol = sorted(colour_data, key=lambda x: x[1]["14d"], reverse=True)
    print()
    print("--- TOP 10 SELLERS (14d volume) ---")
    print(f"{'#':>3s} {'SKU':20s} {'14d':>7s} {'% total':>8s}")
    cumulative = 0
    for i, (sku, d) in enumerate(by_vol[:10]):
        pct = d["14d"] / total_c14 * 100 if total_c14 > 0 else 0
        cumulative += pct
        print(f"{i+1:>3d} {sku:20s} {d['14d']:>7.1f} {pct:>7.1f}%")
    print(f"    {'Top 10 total':20s} {sum(d['14d'] for _, d in by_vol[:10]):>7.1f} {cumulative:>7.1f}%")

    # Top 10 risers (7d vs 30d, minimum 2/d on 14d)
    risers = []
    for sku, d in colour_data:
        if d["14d"] >= 2 and d["30d"] > 0.5:
            accel = pct_change(d["7d"], d["30d"])
            if accel > 5:
                risers.append((sku, d, accel))
    risers.sort(key=lambda x: x[2], reverse=True)
    print()
    print("--- TOP 10 RISERS (7d vs 30d, min 2/d) ---")
    print(f"{'SKU':20s} {'7d':>7s} {'14d':>7s} {'30d':>7s} {'Accel':>8s}")
    for sku, d, accel in risers[:10]:
        print(f"{sku:20s} {d['7d']:>7.1f} {d['14d']:>7.1f} {d['30d']:>7.1f} {accel:>+7.0f}%")
    if not risers:
        print("  (none above threshold)")

    # Top 10 fallers (7d vs 30d, minimum 2/d on 30d)
    fallers = []
    for sku, d in colour_data:
        if d["30d"] >= 2:
            decel = pct_change(d["7d"], d["30d"])
            if decel < -10:
                fallers.append((sku, d, decel))
    fallers.sort(key=lambda x: x[2])
    print()
    print("--- TOP 10 FALLERS (7d vs 30d, min 2/d on 30d) ---")
    print(f"{'SKU':20s} {'7d':>7s} {'14d':>7s} {'30d':>7s} {'Decel':>8s}")
    for sku, d, decel in fallers[:10]:
        print(f"{sku:20s} {d['7d']:>7.1f} {d['14d']:>7.1f} {d['30d']:>7.1f} {decel:>+7.0f}%")
    if not fallers:
        print("  (none above threshold)")

    # Catalogue efficiency
    print()
    print("--- CATALOGUE EFFICIENCY ---")
    cumul = 0
    thresholds = {50: None, 80: None, 90: None}
    for i, (sku, d) in enumerate(by_vol):
        cumul += d["14d"] / total_c14 * 100 if total_c14 > 0 else 0
        for t in thresholds:
            if thresholds[t] is None and cumul >= t:
                thresholds[t] = i + 1
    for t, count in thresholds.items():
        if count is not None:
            print(f"  {count} colours drive {t}% of volume")
    print(f"  Total active (>0 sales 14d): {active_gt0} of {len(colour_data)}")

    # ================================================================
    # REPURCHASE SIGNALS
    # ================================================================
    print()
    print("=" * 65)
    print("REPURCHASE SIGNALS")
    print("=" * 65)

    # Liquid repurchase
    print()
    print("--- LIQUID REPURCHASE ---")
    print(f"  Standalone liquid DSR: 7d={liq7:.1f} | 14d={liq14:.1f} | 30d={liq30:.1f}")
    print(f"  Liquid-to-kit ratio:   {liq_ratio_14:.2f} (14d) | {liq_ratio_30:.2f} (30d)")
    ratio_chg = pct_change(liq_ratio_14, liq_ratio_30)
    if abs(ratio_chg) > 5:
        direction = "up" if ratio_chg > 0 else "down"
        print(f"  Trend: ratio {direction} {abs(ratio_chg):.0f}% — {'more' if direction == 'up' else 'fewer'} repeat purchases relative to new kits")
    else:
        print(f"  Trend: stable")

    # Remove repurchase
    rem7 = sum(get(s)["7d"] for s in acc_remove)
    rem14 = sum(get(s)["14d"] for s in acc_remove)
    rem30 = sum(get(s)["30d"] for s in acc_remove)
    print()
    print("--- REMOVE PRODUCTS (repeat-purchase proxy) ---")
    print(f"  Total remove DSR: 7d={rem7:.1f} | 14d={rem14:.1f} | 30d={rem30:.1f}")

    # Bundle performance
    bun14_total = sum(get(s)["14d"] for s in acc_bundles)
    print()
    print("--- BUNDLE PERFORMANCE ---")
    for sku in acc_bundles:
        d = get(sku)
        if d["14d"] > 0 or d["7d"] > 0:
            chg = pct_change(d["7d"], d["30d"])
            print(f"  {sku:20s}  7d={d['7d']:.1f} | 14d={d['14d']:.1f} | 30d={d['30d']:.1f}  ({chg:+.0f}%)")

    # ================================================================
    # SELLING FLAGS
    # ================================================================
    print()
    print("=" * 65)
    print("SELLING FLAGS")
    print("=" * 65)

    # Breakout performers (all windows rising, min 2/d)
    breakouts = []
    for sku, d in sku_dsr.items():
        if sku.startswith("STO-") or sku in ["ACC-INS", "ACC-THA", "ACC-LAB"]:
            continue
        if d["14d"] >= 2 and d["7d"] > d["14d"] > d["30d"] and d["30d"] > 0.5:
            total_mom = pct_change(d["7d"], d["30d"])
            if total_mom > 10:
                breakouts.append((sku, d, total_mom))
    breakouts.sort(key=lambda x: x[2], reverse=True)
    print()
    print(f"--- BREAKOUT PERFORMERS (sustained growth: 7d > 14d > 30d, min 2/d) ---")
    print(f"{'SKU':20s} {'7d':>7s} {'14d':>7s} {'30d':>7s} {'Momentum':>10s}")
    for sku, d, mom in breakouts[:15]:
        print(f"{sku:20s} {d['7d']:>7.1f} {d['14d']:>7.1f} {d['30d']:>7.1f} {mom:>+9.0f}%")
    if not breakouts:
        print("  (none)")

    # Fading performers (all windows declining, min 2/d on 30d)
    fading = []
    for sku, d in sku_dsr.items():
        if sku.startswith("STO-") or sku in ["ACC-INS", "ACC-THA", "ACC-LAB"]:
            continue
        if d["30d"] >= 2 and d["7d"] < d["14d"] < d["30d"]:
            total_fade = pct_change(d["7d"], d["30d"])
            if total_fade < -10:
                fading.append((sku, d, total_fade))
    fading.sort(key=lambda x: x[2])
    print()
    print(f"--- FADING PERFORMERS (sustained decline: 7d < 14d < 30d, min 2/d) ---")
    print(f"{'SKU':20s} {'7d':>7s} {'14d':>7s} {'30d':>7s} {'Fade':>10s}")
    for sku, d, fade in fading[:15]:
        print(f"{sku:20s} {d['7d']:>7.1f} {d['14d']:>7.1f} {d['30d']:>7.1f} {fade:>+9.0f}%")
    if not fading:
        print("  (none)")

    # Spikes (7d > 30d by 50%+, min 1/d on 30d)
    spikes = []
    for sku, d in sku_dsr.items():
        if sku.startswith("STO-") or sku in ["ACC-INS", "ACC-THA", "ACC-LAB"]:
            continue
        if d["30d"] >= 1 and d["7d"] > 0.5:
            spike = pct_change(d["7d"], d["30d"])
            if spike >= 50:
                spikes.append((sku, d, spike))
    spikes.sort(key=lambda x: x[2], reverse=True)
    print()
    print(f"--- SPIKES (7d > 30d by 50%+, min 1/d) ---")
    print(f"{'SKU':20s} {'7d':>7s} {'14d':>7s} {'30d':>7s} {'Spike':>8s}")
    for sku, d, spike in spikes[:10]:
        print(f"{sku:20s} {d['7d']:>7.1f} {d['14d']:>7.1f} {d['30d']:>7.1f} {spike:>+7.0f}%")
    if not spikes:
        print("  (none)")
    if spikes:
        print("  Check #sale-announcements and #cro-team-meetings for context")

    # Drops (7d < 30d by 40%+, min 2/d on 30d)
    drops = []
    for sku, d in sku_dsr.items():
        if sku.startswith("STO-") or sku in ["ACC-INS", "ACC-THA", "ACC-LAB"]:
            continue
        if d["30d"] >= 2:
            drop = pct_change(d["7d"], d["30d"])
            if drop <= -40:
                drops.append((sku, d, drop))
    drops.sort(key=lambda x: x[2])
    print()
    print(f"--- DROPS (7d < 30d by 40%+, min 2/d) ---")
    print(f"{'SKU':20s} {'7d':>7s} {'14d':>7s} {'30d':>7s} {'Drop':>8s}")
    for sku, d, drop in drops[:10]:
        print(f"{sku:20s} {d['7d']:>7.1f} {d['14d']:>7.1f} {d['30d']:>7.1f} {drop:>+7.0f}%")
    if not drops:
        print("  (none)")
    if drops:
        print("  Check OOS status, listing changes, post-promo normalisation")


if __name__ == "__main__":
    main()
