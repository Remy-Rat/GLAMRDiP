# AUS Sales Data Analysis — 11 May 2026

## DATA FRESHNESS

- **Shopify:** through 10 May (+1d lag, normal). 7d = 4-10 May. 14d = 27 Apr-10 May. 30d = 11 Apr-10 May.
- **3PL (AUS 3GPL):** last valid 11 May (today).
- **Growth factor:** 1.3x. POS MODEL base 147/d → scaled 191.1/d.
- **POS MODEL UPDATED:** cell not filled today (assumed AM paste).

---

## HEADLINE — THE -17% RECOVERY IS REAL AND IS KIT-COM-4

W19 (4-10 May) Shopify kit sales **172.7/d**, a **+141% week-over-week jump** from W18's 71.7/d. The recovery is overwhelmingly **Complete kits**:

| Kit | 7d | 14d | 30d | 7d vs 30d |
|---|---:|---:|---:|---:|
| KIT-STA-2 | 24.9 | 22.8 | 25.2 | **-1% (FLAT)** |
| **KIT-COM-4** | **114.4** | 73.5 | 60.8 | **+88%** |
| KIT-ULT-6 | 33.4 | 25.9 | 22.5 | +48% |
| **TOTAL** | **172.7** | 122.2 | 108.5 | +59% |

**Implications for 08072026 sizing (place 18-25 May):**
- 7d effective growth factor: 172.7 / 147 = **1.17x** (vs 1.3x target → -10%).
- 14d effective growth factor: 122.2 / 147 = **0.83x** (-36%).
- 30d effective growth factor: 108.5 / 147 = **0.74x** (-43%).
- **STA mix is dropping fast** (14% of W19 kits vs 23% of 30d). Don't size 08072026 STA up — current OL 1,372 is already generous at recovered rate.
- **COM mix is the story** (66% of W19 vs 56% of 30d). Hold or modestly increase COM OL on 08072026 (sheet 3,192).
- **ULT mix steady** (19% of W19 vs 21% of 30d). The earlier ULT-cut recommendation stands at 30-40%.

**Need cross-reference:** the KIT-COM-4 surge needs a marketing/CRO explanation. Daniel 8 May referenced kit offer change to reduce double-consignment — that's a backend logistics tweak, not a demand driver. Likely candidates: GWP campaign uptake (launched 3 May, AUS-$85-GIF), Mother's Day timing (11 May), or undocumented promo. **Sale-announcements / CRO channels not yet checked.**

---

## DSR: MODEL vs REALITY

### KITS

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | 3PL 14d | Gap (Model vs 14d) |
|---|---:|---:|---:|---:|---:|---:|
| KIT-STA-2 | 44.2 | 24.9 | 22.8 | 25.2 | 22.7 | -48% |
| KIT-COM-4 | 101.4 | 114.4 | 73.5 | 60.8 | 72.4 | -28% |
| KIT-ULT-6 | 45.5 | 33.4 | 25.9 | 22.5 | 26.1 | -43% |

**Shopify vs 3PL alignment for kits is near-perfect** (gaps 0.1-1.1/d). The data integrity is sound — Daniel's 7 May "DSR oversells post-website-switch" concern does not appear in AUS 3PL deductions matching Shopify.

### HEAL (kit-adjusted at G3PL)

| Metric | Value |
|---|---:|
| Shopify standalone 14d | 3.1/d |
| 3PL deductions 14d | 125.3/d |
| Implied kit-attached | 122.2/d |
| Sum of Shopify kit 14d DSR | 122.2/d (STA 22.8 + COM 73.5 + ULT 25.9) |

**Heal kit-attached deduction matches Shopify kit sales EXACTLY** (1 Heal per kit). Heal data integrity perfect.

At 7d kit rate (172.7/d) + standalone 3.0/d → Heal demand = **175.7/d**. POS MODEL DSR 184.6 is now accurate-to-slightly-conservative (was -33% under-stating at 14d).

### LIQUIDS (standalone — pre-packed in kits from China)

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | 3PL 14d | Notes |
|---|---:|---:|---:|---:|---:|---|
| LIQ-BAS-2 (Base) | 53.3 | **37.1** | 32.4 | 24.2 | 37.7 | 7d +53% vs 30d, OOS now |
| LIQ-SEN-2 (LO Base) | 9.1 | 0.0 (OOS) | 4.1 | 4.2 | 9.0 | **3PL 9.0/d much higher than Shopify 4.1/d** — bundle leakage? |
| LIQ-GLO-4 (Glow) | 26.0 | 18.9 | 14.1 | 10.7 | 15.9 | 7d +77% vs 30d |
| LIQ-SEN-4 (LO Glow) | 7.8 | 6.6 | 6.3 | 4.3 | 7.2 | 7d +53% vs 30d |
| LIQ-SEA-3 (Seal) | 44.2 | 25.7 | 21.9 | 16.4 | 24.2 | 7d +57% vs 30d |
| LIQ-BON-1 (Bond) | 16.9 | 9.4 | 7.6 | 6.0 | 9.2 | 7d +57% vs 30d |
| LIQ-SOA-6 (Sensitive Glow) | 13.0 | 4.9 | 4.1 | 4.2 | 5.8 | flat |

**Every liquid except Sensitive Glow shows 7d rate +50-77% above 30d** — consistent with kit-driven demand surge (most liquids are kit-attached components).

**Sensitive Base discrepancy:** Shopify standalone 4.1/d but 3PL 9.0/d. LIQ-SEN-2 isn't in any bundle. The 9.0/d 3PL rate must be partially fed by LIQ-SET bundle deductions (Liquids Set contains 6 liquids — but LIQ-SET sells at only 1.1/d, so contributes 1.1/d to LIQ-SEN-2 deduction). 4.1 + 1.1 = 5.2, still short of 9.0. Possible explanation: a quarantine/disposal event or kit composition unclear. **Surface to Greg/Daniel.**

### REMOVE / BUNDLES

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | 3PL 14d |
|---|---:|---:|---:|---:|---:|
| ACC-REM (120ml) | 33.8 | 6.6 | 6.3 | 8.0 | 42.2 |
| ACC-REM-500 | 98.8 | **79.7** | 51.1 | 36.2 | 68.0 |
| ACC-REM-BOW | 75.4 | 4.6 | 2.9 | 2.8 | 53.8 |
| ACC-REM-BUN-1 (120ml+Bowl) | n/a | **56.1** | 33.6 | 19.7 | n/a |
| ACC-REM-BUN-2 (500ml+Bowl) | n/a | 17.6 | 17.0 | 19.9 | n/a |
| LIQ-SET (Liquids Set) | n/a | 1.3 | 1.1 | 1.4 | n/a |

**Daniel's 7 May "oversells" decoded:**
- **"Base +54%":** LIQ-BAS-2 Shopify 7d 37.1/d vs 30d 24.2/d → +53% ✓
- **"Remove 120ml +122%":** Actually the BUNDLE — ACC-REM-BUN-1 7d 56.1/d vs 30d 19.7/d → **+185%.** Standalone ACC-REM at 6.6/d is flat.
- **"Remove Bowl +32%":** ACC-REM-BOW Shopify 7d 4.6/d vs 30d 2.8/d → +64% (standalone only); combined with bundles total is 78.3/d at 7d rate.

**ACC-REM-BOW total demand at 7d rate:**
- Standalone 4.6 + BUN-1 56.1 + BUN-2 17.6 = **78.3/d**
- Stock 480 / 78.3/d = **6 days cover** (tighter than the 9d POS Check calculated at 14d rate).
- OOS roughly **17 May** (6 days from today). AUS 09052026 arrives 40 days from now → **34-day OOS gap** at recent run rate.
- **Per user: accept OOS, no cross-region bridge.**

**ACC-REM-500 surge:** standalone 79.7/d at 7d + BUN-2 component 17.6/d = 97.3/d combined demand. Stock 7,106 / 97.3 = **73 days cover** (was 104d at 14d rate). Still safe to 13 Jul; AUS 08072026 brings 5,000 ACC-RE5-BOT/LID/INN for next OP fill. **Plan next OP Remove 500ml fill ~early Jul.**

---

## WEEKLY KIT TREND

| Week | Dates | Days | Kits | Daily | vs 1.3x (191) | vs 1.0x (147) |
|---|---|---:|---:|---:|---:|---:|
| W11 | 9-15 Mar | 7 | 737 | 105.3 | -45% | -28% |
| W12 | 16-22 Mar | 7 | 912 | 130.3 | -32% | -11% |
| W13 | 23-29 Mar | 7 | 899 | 128.4 | -33% | -13% |
| W14 | 30 Mar-5 Apr | 7 | 738 | 105.4 | -45% | -28% |
| W15 | 6-12 Apr | 7 | 947 | 135.3 | -29% | -8% |
| W16 | 13-19 Apr | 6 | 618 | 103.0 | -46% | -30% |
| W17 | 20-26 Apr | 7 | 605 | 86.4 | -55% | -41% |
| W18 | 27 Apr-3 May | 7 | 502 | 71.7 | -62% | -51% |
| **W19** | **4-10 May** | **7** | **1,209** | **172.7** | **-10%** | **+17%** |

**W19 is the strongest week in the entire 9-week post-transition period.** Bypasses W15 (135) and W12 (130). Even W18→W19 jump (+101 kits/d) exceeds the W14→W15 Easter sale lift (+30/d).

**Trend interpretation:**
- 3 escalating weeks down (W15→W16→W17→W18 floor at 71.7).
- W19 reverses entire decline trajectory.
- Either (a) genuine sustained recovery (post-website-switch fix, GWP uptake, Mother's Day pull-forward), (b) one-off promo or campaign spike that will normalise back to W17-W18 floor.
- **Verdict cannot be made on a single week.** Treat as inflection signal — fold into 08072026 sizing with cushion (don't fully revert to 1.3x sizing yet; don't deep-cut as if W18 is the new floor either).

### KIT MIX

| Period | STA % | COM % | ULT % |
|---|---:|---:|---:|
| 30d | 23% | 56% | 21% |
| 14d | 19% | 60% | 21% |
| **7d (W19)** | **14%** | **66%** | **19%** |

**STA is structurally trailing.** Even at the kit-recovery peak, STA stays flat in absolute terms while COM doubles. AUS 08072026 STA OL of 1,372 is right-sized; AUS 09052026 STA OL of 2,016 may run hot if W19 normalises lower.

---

## REALISTIC DAYS COVER

| SKU | Stock | DSR used | Cover | Flag |
|---|---:|---|---:|---|
| LIQ-BAS-2 | 0 | 37.1 (Shop 7d) | OOS | 🔴 |
| LIQ-SEN-2 | 0 | 9.0 (3PL 14d, Shop 0) | OOS | 🔴 |
| ACC-REM-BOW | 480 | 78.3 (total 7d) | **6d** | 🔴 (per user, accepted OOS) |
| LIQ-SEN-4 | 56 | 7.2 (3PL 14d) | 8d | 🟡 |
| KIT-STA-2 | 708 | 22.7 (Shop 14d / 3PL 14d) | 31d | 🟡 (recovered rate: 25/d → 28d) |
| LIQ-GLO-4 | 606 | 18.9 (Shop 7d) | 32d | 🟡 (was 38d at 14d) |
| KIT-COM-4 | 3,584 | 114.4 (Shop 7d) | **31d** | 🟡 (was 49d at 14d — recent rate compresses cover) |
| ACC-LAB | 13,719 | 219/d (3PL 14d) | 63d | 🟢 (Avi PO this week) |
| LIQ-HEA-5 | 8,165 | 175.7 (7d kit-adj) | 46d | 🟢 (22-04-2026 fill landing ~10 Jul) |

**KIT-COM-4 newly tight at recovered rate.** 3,584 / 114.4 = 31d cover. AUS 09052026 in 40 days at 3,052 OL → **9-day OOS gap if W19 demand holds.** Sales Analysis flag: COM is now the kit-side risk alongside STA, not just STA.

---

## CONTAINER ARRIVALS DETECTED (3PL data)

3 recent multi-SKU arrival days detected:
- **28 Mar** — 95 SKUs / 84,008 units. Top: ACC-INS, ACC-5PC-BAG, ACC-RE1-LID, ACC-REM, STO-MAI-BAG-S. (Powder Room/early fill setup.)
- **10 Apr** — 118 SKUs / 128,553 units. Top: ACC-THA, ACC-INS, STO-MAI-BAG-S, STO-MAI-2, ACC-RE5-BOT. (Likely AUS 09032026 powder/components landing.)
- **14 Apr** — 197 SKUs / 194,695 units. Top: POW-CLE-193 (39,068!), ACC-STI-45885, POW-BOU-222, ACC-REM, POW-HEA-515. (B360 PACKUP main transfer event.)

No new container arrivals since 14 Apr.

---

## INVENTORY DISCREPANCIES

### Cumulative gap test (30d) — clean

Only two colour SKUs show 3PL > Shopify by 300+ units over 30d, both explained:
- **POW-SUN-SU015:** 3PL 30d 4,353 vs Shop 30d 12 → gap 4,341. **GWP component (AUS-$85-GIF).** Benign.
- **POW-CLE-193:** 3PL 30d 4,176 vs Shop 30d 1,206 → gap 2,970. **GWP component.** Benign.

The 22,090-unit unexplained colour cumulative gap from the 17 Apr review has not recurred. POW-ENE-484, POW-DRE-771, POW-ROY-304, POW-JUS-449, POW-GOL-597, POW-BRE-109, POW-CRE-217 all show normal patterns in the last 30 days. **Clean — that batch was a one-off event, not ongoing leakage.**

### Open from PO 9 B360 PACKUP (still pending Jake count)

23-SKU variance list emailed 28 Apr, count overdue 14 days:
- -9,376 ACC-RE1-BOT
- -911 ACC-REM-500
- +1,867 ACC-STI-45885 (over)
- -200 each on 11 colour SKUs (Sincere, Cosmic, Fairytale, Holly, Melody, Rustle, Sweet Tooth, Violet Sky, Ghostin, Creme Brulee -250)
- Plus the **1,300pcs Heal mystery** (likely separate to PO 9 per 7 May Slack)

These remain open. Sales Analysis cannot close them — needs G3PL recount.

### LIQ-SEN-2 anomaly (raised in liquids section)

3PL 9.0/d vs Shopify 4.1/d standalone, no clean bundle pairing to explain. Surface to Greg/Daniel.

---

## 3PL DEDUCTION CHECK (Shopify vs 3PL alignment)

| SKU | Shop 14d | 3PL 14d | Gap | Status |
|---|---:|---:|---:|---|
| KIT-STA-2 | 22.8 | 22.7 | +0.1 | Aligned |
| KIT-COM-4 | 73.5 | 72.4 | +1.1 | Aligned |
| KIT-ULT-6 | 25.9 | 26.1 | -0.2 | Aligned |

**Kit deduction integrity is perfect.** Daniel's 7 May "DSR oversell" concern does not appear in AUS kit data. The website-switch noise may be elsewhere — Sales Performance check might surface it on standalone product pages.

---

## SELLING PERFORMANCE FLAGS

### COLOUR SPIKES (7d > 30d by 50%+, 7d ≥ 5/d)

29 colour SKUs spiking. Top 10 by volume:

| SKU | 7d | 30d | Spike | Cover @ 7d |
|---|---:|---:|---:|---:|
| POW-POS-184 | 52.1 | 29.8 | +75% | 77d |
| POW-HEA-515 | 53.6 | 33.2 | +61% | 100d |
| POW-PIL-194 | 48.0 | 27.9 | +72% | 56d |
| POW-GOD-017 | 26.6 | 14.8 | +80% | 114d |
| POW-BLA-384 | 26.0 | 17.0 | +53% | 113d |
| POW-CHA-011 | 25.9 | 10.4 | +149% | 57d |
| POW-TRA-452 | 21.9 | 14.0 | +56% | 122d |
| POW-BAR-198 | 21.9 | 12.5 | +75% | 183d |
| POW-SLO-192 | 21.1 | 13.1 | +61% | 161d |
| POW-EMB-602 | 18.9 | 10.8 | +75% | n/a |

**Notable:**
- **POW-GOD-017 (Goddess):** +80% spike. Stock 3,036, 114d cover at 7d rate. Carryover from 4 May (was flagged as collapsed 59%). **Listing or marketing change may have fixed.**
- **POW-BLU-ZGD22 (Blue Moon):** +119% spike (7d 7.9/d vs 30d 3.6/d). Was OOS-on-website 4+ weeks. **Stock 514 / 7.9 = 65d cover.** Active sales suggest listing has been re-enabled. Confirm with Joel/Remy.
- **POW-CHA-011 (Charming):** +149% spike off a low base. 98d cover at 7d rate.

### COLOUR DROPS (7d < 30d by 40%+, 30d ≥ 4/d)

| SKU | 7d | 30d | Drop |
|---|---:|---:|---:|
| POW-STA-033 | 1.0 | 6.6 | -85% |
| POW-MIL-193 | 1.0 | 5.9 | -83% |
| POW-DUS-346 | 3.4 | 10.7 | -68% |
| POW-DRE-771 | 1.6 | 4.8 | -67% |
| POW-ROY-304 | 2.3 | 6.5 | -65% |
| POW-SEA-450 | 1.9 | 5.5 | -65% |
| POW-ILL-001 | 2.0 | 4.8 | -58% |
| POW-OUR-772 | 4.6 | 8.0 | -43% |
| POW-CRU-090 | 2.4 | 4.2 | -43% |

**Investigate:** POW-STA-033, POW-MIL-193, POW-DUS-346 — large drops, likely listing or stock issue. Check Shopify availability.

### COLOURS WITH ZERO SHOPIFY 14d SALES (25 SKUs)

**Listing audit candidates:**

- **Fire Collection (8 SKUs):** POW-SAF-149, POW-RED-165, POW-ALL-146, POW-INF-506, POW-BOR-355, POW-GAR-656, POW-HOT-568, POW-SPI-144. Carryover from 4+ weeks. **Still unresolved.**
- **W-suffix (winter limited?) (8 SKUs):** POW-DAW-W015, POW-GRA-W036, POW-IGN-W021, POW-MEC-W039, POW-PUL-W035, POW-THE-W005, POW-TID-W006, POW-EUP-014. Likely seasonal — confirm listing state.
- **Other (9 SKUs):** POW-AUR-023, POW-ENI-024, POW-GLO-018, POW-LUM-021, POW-MIR-015, POW-SOL-019, POW-LIM-LH10, POW-BLU-D22, POW-BLU-ZGDD22.

Likely listing or unlaunched. Bandwidth-light dead-stock audit — Gav/Remy when bandwidth allows.

### SENSITIVE BASE / LO BASE / LO GLOW MIX

| Pair | Regular 14d | LO 14d | LO mix |
|---|---:|---:|---:|
| Base vs LO Base | 32.4 | 4.1 | **13%** |
| Glow vs LO Glow | 14.1 | 6.3 | **45%** |

LO Base mix is much lower than expected (POS MODEL ~30% target). LO Glow mix is high. Sizing in containers:
- AUS 05052026: 648 Base / 216 LO Base = 33% LO mix — **oversized for LO Base** (actual demand only 13%).
- AUS 09052026: 2,592 Base / 432 LO Base = 17% LO mix — closer to actual but still slight over.
- AUS 09052026: 1,296 Glow / 432 LO Glow = 33% LO Glow mix — undersized vs actual 45%.

**ACTION:** Cut LO Base on future containers from 33% → 15%. Increase LO Glow allocation to 40-45%.

---

## KEY TAKEAWAYS

1. **W19 (4-10 May) Shopify kit sales 172.7/d — a +141% week-over-week recovery.** Whole reversal of the W14→W18 decline. KIT-COM-4 +88% vs 30d is the dominant driver; STA flat; ULT +48%. Either real sustained recovery or one-off spike — needs another week to confirm.

2. **Data integrity sound.** Shopify kit DSR matches 3PL deductions within 1.1/d for all three kits. Heal kit-attached deduction matches Shopify kit sales exactly. Daniel's "DSR oversell" concern is not visible in AUS deduction data — likely a website-display issue, not stock-pull issue.

3. **08072026 sizing recommendation:** hold STA (recovered rate +0%, sheet 1,372 right-sized); hold or +5% COM (sheet 3,192 right); trim ULT 25-30% (recovered rate +48% but absolute volume still low). Treat 1.0x effective as floor scenario, 1.17x as upper for sizing buffer.

4. **ACC-REM-BOW will OOS ~17 May.** At 7d combined demand 78.3/d, stock 480 lasts 6 days; container 34 days away. Per user, accept OOS — no bridge. **Plan: communicate to Gav/CX about the gap for bundle-customer expectations.**

5. **KIT-COM-4 now tight too at recovered rate.** 31d cover vs AUS 09052026 in 40 days → 9d OOS gap if W19 holds. Watch this week — second week of 100+/d COM demand means escalate, otherwise the 14d view stabilises.

6. **Multiple colour spikes (+50-150%)** without obvious campaign trigger. Likely flows from kit-buying surge driving colour mix into top-sellers (POW-POS-184, POW-HEA-515, POW-PIL-194). All still 56-100d+ cover so no SKU at immediate risk. Check `#sale-announcements` and `#cro-team-meetings` for context.

7. **Listing audit overdue:** 8 Fire Collection SKUs zero-sale 4+ weeks. Blue Moon now selling at 7.9/d (suggests relist done). POW-STA-033 / POW-MIL-193 dropped 80%+ — verify listings still live.

8. **LIQ-SEN-2 3PL 9/d vs Shopify 4.1/d** — small unexplained variance. Surface to Greg.

9. **LO Base mix is 13%, not 30% — undersize LO Base** in future containers. LO Glow mix 45% — undersize regular Glow OR oversize LO Glow.

10. **The PO 9 B360 PACKUP 23-SKU variance count remains open** (Jake's 1 May commitment 14 days overdue). Sales Analysis cannot resolve — needs G3PL escalation.
