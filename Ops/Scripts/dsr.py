"""
dsr.py — DSR comparison tables (model vs actual Shopify).

Usage:
    uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py AUS | \
    uv run --with pandas python3 Ops/Scripts/dsr.py

Reads extracted JSON from stdin. Outputs formatted DSR comparison tables.
"""

import sys
import json


def main():
    data = json.load(sys.stdin)
    region = data["region"]
    pos = data["pos_model"]
    shop = data["shopify"]
    config = data["config"]

    growth_factor = pos["growth_factor"]
    kit_base = pos["kit_dsr_base"]
    kit_scaled_total = pos["kit_scaled_total"]
    kit_base_total = pos["kit_base_total"]
    products = {p["sku"]: p for p in pos["products"]}
    sku_dsr = shop["sku_dsr"]

    print(f"DSR: MODEL vs REALITY — {region} — extracted {data['extracted_at']}")
    print(f"Growth factor: {growth_factor}x | Base: {kit_base_total:.0f}/d | Scaled: {kit_scaled_total:.1f}/d")
    print(f"Shopify latest: {shop['latest_date']}")
    print()

    # ---- Kits ----
    print("--- KITS ---")
    print(f"{'SKU':15s} {'Model DSR':>10s} {'Shop 7d':>8s} {'Shop 14d':>9s} {'Shop 30d':>9s} {'Gap 14d':>8s}")
    kit_actual_14d = 0
    kit_actual_7d = 0
    for sku in ["KIT-STA-2", "KIT-COM-4", "KIT-ULT-6"]:
        m = products.get(sku, {}).get("model_dsr", 0)
        s = sku_dsr.get(sku, {"7d": 0, "14d": 0, "30d": 0})
        kit_actual_14d += s["14d"]
        kit_actual_7d += s["7d"]
        gap = ((s["14d"] - m) / m * 100) if m > 0 else 0
        print(f"{sku:15s} {m:>10.1f} {s['7d']:>8.1f} {s['14d']:>9.1f} {s['30d']:>9.1f} {gap:>+7.0f}%")
    print(f"{'TOTAL':15s} {kit_scaled_total:>10.1f} {kit_actual_7d:>8.1f} {kit_actual_14d:>9.1f}")

    actual_gf = kit_actual_14d / kit_base_total if kit_base_total > 0 else 0
    rec_gf = actual_gf * 1.1
    vs_target = ((kit_actual_14d / kit_scaled_total) - 1) * 100 if kit_scaled_total else 0
    print(f"\nActual growth: {actual_gf:.2f}x | Recommended (actual+10%): {rec_gf:.2f}x | vs target: {vs_target:+.1f}%")

    # ---- Kit Mix ----
    print(f"\n--- KIT MIX (14d) ---")
    for sku in ["KIT-STA-2", "KIT-COM-4", "KIT-ULT-6"]:
        s14 = sku_dsr.get(sku, {}).get("14d", 0)
        base = kit_base.get(sku, 0)
        scaled = base * growth_factor if growth_factor else 0
        pct = (s14 / kit_actual_14d * 100) if kit_actual_14d > 0 else 0
        gap = ((s14 / scaled) - 1) * 100 if scaled > 0 else 0
        print(f"  {sku}: {s14:.1f}/d ({pct:.0f}% of total) | Base: {base:.0f} | Scaled: {scaled:.1f} | Gap: {gap:+.0f}%")

    # ---- Heal (kit-adjusted) ----
    print(f"\n--- HEAL (kit-adjusted: standalone + kit consumption at 3PL) ---")
    sku = "LIQ-HEA-5"
    m = products.get(sku, {}).get("model_dsr", 0)
    s = sku_dsr.get(sku, {"7d": 0, "14d": 0, "30d": 0})
    adj14 = s["14d"] + kit_actual_14d
    adj7 = s["7d"] + kit_actual_7d
    gap = ((adj14 - m) / m * 100) if m > 0 else 0
    print(f"  Model: {m:.1f}/d | Standalone 7d: {s['7d']:.1f} | Standalone 14d: {s['14d']:.1f}")
    print(f"  Kit-adj 7d: {adj7:.1f} | Kit-adj 14d: {adj14:.1f} | Gap vs model: {gap:+.0f}%")

    # ---- Liquids (standalone) ----
    liquid_skus = ["LIQ-BAS-2", "LIQ-SEN-2", "LIQ-SEA-3", "LIQ-GLO-4", "LIQ-SEN-4", "LIQ-BON-1", "LIQ-MAT-4", "LIQ-SOA-6"]
    print(f"\n--- LIQUIDS (standalone — pre-packed in kits from CN) ---")
    print(f"{'SKU':15s} {'Model DSR':>10s} {'Shop 7d':>8s} {'Shop 14d':>9s} {'Shop 30d':>9s} {'Gap 14d':>8s}")
    for sku in liquid_skus:
        m = products.get(sku, {}).get("model_dsr", 0)
        s = sku_dsr.get(sku, {"7d": 0, "14d": 0, "30d": 0})
        gap = ((s["14d"] - m) / m * 100) if m > 0 else 0
        # Mark kit-adjusted items for this region
        ka = " *KA*" if sku in config["kit_adjusted_items"] else ""
        print(f"{sku:15s} {m:>10.1f} {s['7d']:>8.1f} {s['14d']:>9.1f} {s['30d']:>9.1f} {gap:>+7.0f}%{ka}")

    # ---- Remove products ----
    print(f"\n--- REMOVE PRODUCTS (standalone) ---")
    print(f"{'SKU':15s} {'Model DSR':>10s} {'Shop 7d':>8s} {'Shop 14d':>9s} {'Shop 30d':>9s} {'Gap 14d':>8s}")
    for sku in ["ACC-REM", "ACC-REM-500", "ACC-REM-BOW"]:
        m = products.get(sku, {}).get("model_dsr", 0)
        s = sku_dsr.get(sku, {"7d": 0, "14d": 0, "30d": 0})
        gap = ((s["14d"] - m) / m * 100) if m > 0 else 0
        print(f"{sku:15s} {m:>10.1f} {s['7d']:>8.1f} {s['14d']:>9.1f} {s['30d']:>9.1f} {gap:>+7.0f}%")

    # ---- Top 20 colours ----
    colour_data = [(sku, d) for sku, d in sku_dsr.items() if sku.startswith("POW-")]
    colour_data.sort(key=lambda x: x[1].get("14d", 0), reverse=True)
    print(f"\n--- TOP 20 COLOURS (by 14d volume) ---")
    print(f"{'SKU':20s} {'Model DSR':>10s} {'Shop 7d':>8s} {'Shop 14d':>9s} {'Shop 30d':>9s} {'Gap 14d':>8s}")
    for sku, d in colour_data[:20]:
        m = products.get(sku, {}).get("model_dsr", 0)
        gap = ((d["14d"] - m) / m * 100) if m > 0 else 0
        print(f"{sku:20s} {m:>10.1f} {d['7d']:>8.1f} {d['14d']:>9.1f} {d['30d']:>9.1f} {gap:>+7.0f}%")

    total_colour_14d = sum(d.get("14d", 0) for _, d in colour_data)
    total_colour_7d = sum(d.get("7d", 0) for _, d in colour_data)
    print(f"\nTotal colour DSR: 7d={total_colour_7d:.1f} | 14d={total_colour_14d:.1f}")

    # ---- LIQ-SET bundle check ----
    liq_set = sku_dsr.get("LIQ-SET", {"7d": 0, "14d": 0, "30d": 0})
    if liq_set["14d"] > 0:
        print(f"\n--- BUNDLE: LIQ-SET ---")
        print(f"  7d: {liq_set['7d']:.1f} | 14d: {liq_set['14d']:.1f} | 30d: {liq_set['30d']:.1f}")
        print(f"  Each sale deducts 1x of all 6 liquids at 3PL. Accounts for ~{liq_set['14d']:.0f}/d of 3PL-Shopify gap per liquid.")

    # ---- Weekly kit trend ----
    print(f"\n--- WEEKLY KIT TREND ---")
    print(f"{'Week':>6s} {'Dates':>22s} {'Days':>5s} {'Total':>7s} {'Daily':>7s} {'vs Model':>9s}")
    for w in shop["weekly_kit_trend"]:
        vs = ((w["daily_rate"] / kit_scaled_total) - 1) * 100 if kit_scaled_total else 0
        print(f"W{w['week']:>4d} {w['dates']:>22s} {w['days']:>5d} {w['total']:>7d} {w['daily_rate']:>7.1f} {vs:>+8.1f}%")

    # ---- Sensitive Base signal ----
    bas14 = sku_dsr.get("LIQ-BAS-2", {}).get("14d", 0)
    sen14 = sku_dsr.get("LIQ-SEN-2", {}).get("14d", 0)
    total_base = bas14 + sen14
    if total_base > 0:
        print(f"\n--- SENSITIVE BASE SIGNAL ---")
        print(f"  Base: {bas14:.1f}/d ({bas14/total_base*100:.0f}%) | Sensitive: {sen14:.1f}/d ({sen14/total_base*100:.0f}%) | Total: {total_base:.1f}/d")

    # ---- Selling flags ----
    print(f"\n--- SALES SPIKES (7d > 30d by 50%+) ---")
    spikes = []
    for sku, d in sku_dsr.items():
        if sku.startswith("STO-") or sku in ["ACC-INS", "ACC-THA", "ACC-LAB"]:
            continue
        if d["30d"] > 0.5 and d["7d"] > 0.5:
            spike = ((d["7d"] / d["30d"]) - 1) * 100
            if spike >= 50:
                spikes.append((sku, d["7d"], d["14d"], d["30d"], spike))
    spikes.sort(key=lambda x: x[4], reverse=True)
    print(f"{'SKU':20s} {'7d':>7s} {'14d':>7s} {'30d':>7s} {'Spike':>7s}")
    for sku, s7, s14, s30, spike in spikes[:10]:
        print(f"{sku:20s} {s7:>7.1f} {s14:>7.1f} {s30:>7.1f} {spike:>+6.0f}%")

    print(f"\n--- SALES DROPS (7d < 30d by 40%+) ---")
    drops = []
    for sku, d in sku_dsr.items():
        if sku.startswith("STO-") or sku in ["ACC-INS", "ACC-THA", "ACC-LAB"]:
            continue
        if d["30d"] > 1.0:
            drop = ((d["7d"] / d["30d"]) - 1) * 100
            if drop <= -40:
                drops.append((sku, d["7d"], d["14d"], d["30d"], drop))
    drops.sort(key=lambda x: x[4])
    print(f"{'SKU':20s} {'7d':>7s} {'14d':>7s} {'30d':>7s} {'Drop':>7s}")
    for sku, s7, s14, s30, drop in drops[:15]:
        print(f"{sku:20s} {s7:>7.1f} {s14:>7.1f} {s30:>7.1f} {drop:>+6.0f}%")

    # ---- Dead stock ----
    dead = []
    for sku in shop["colours_14d_zero"]:
        p = products.get(sku)
        if p and p["g3pl_on_hand"] > 0:
            dead.append((sku, p["g3pl_on_hand"]))
    dead.sort(key=lambda x: x[1], reverse=True)
    print(f"\n--- DEAD STOCK (colours: in stock, 0 Shopify 14d) ---")
    print(f"Count: {len(dead)} | Total units: {sum(s for _, s in dead):,}")
    for sku, stock in dead[:10]:
        print(f"  {sku}: {stock:,}")


if __name__ == "__main__":
    main()
