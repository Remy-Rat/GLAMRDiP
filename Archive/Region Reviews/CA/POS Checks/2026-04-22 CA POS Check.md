# POS MODEL CHECK — CA — 22 Apr 2026

## DATA FRESHNESS
- **POS MODEL updated:** 22 Apr 2026 (today — fresh paste)
- **3PL data last valid:** 22 Apr 2026
- **Shopify latest:** ~20 Apr 2026
- **Growth factor:** 1.5x (base 80/d → scaled 120/d) — **UPDATED from 2.0x since last review**
- **ShipHero exports:** None (247 uses different system; 3PL tab is the live view)

## MANUAL OVERRIDES / SAME-DAY RECONCILIATION

User confirmed 22 Apr:
- **Swift fill checked in at 247:** LIQ-HEA-5 +7,500 (1,239 → 8,880), ACC-REM-500 +3,644 (0 → 3,644). POS MODEL container line removed. Already reflected in today's paste.
- **CA 03022026 + CA 07042026 still held at customs.** Status in POS MODEL still "On the Way". Remy/Joel following up separately.

### DATA ARTEFACT OVERRIDES — Greg's paste glitches 11-16 Apr

Three single-day stock drops in the 3PL data are paste errors, not deductions. Stock recovered next day. The forecast script's 14d DSR for these SKUs is distorted and must be overridden:

| SKU | Glitch | True 14d trend | Script output | Corrected |
|---|---|---|---|---|
| POW-MOO-401 (Mood) | 11 Apr: 1,102 → 1 → 1,097 | 2.2/d | "9d cover CRITICAL" | **~500d cover — SAFE** |
| POW-RAD-043 (Radiant) | 11-13 Apr: 829 → 0 → 731 | Artefact from SKU rename | "6d cover CRITICAL" | **~50-60d cover — see below** |
| STO-MAI-2 (Small Box) | 13 Apr: 11,095 → 18 → 10,933 | 47.7/d true | "11d CRITICAL" | **~225d cover — SAFE** |
| STO-BUB-BAG-L (Bubble Mailer) | 15-16 Apr: 10,216 → 83 → 32 → 9,974 | 55.0/d true | "11d CRITICAL" | **~177d cover — SAFE** |

Multiple other 1,000-unit single-day deductions in March (POW-DAY, POW-TEM, POW-SHH, POW-SWE, POW-ECL, POW-IMA, POW-PUM) appear to be the same pattern. These are Greg's paste issues, not real demand.

---

## STOCK POSITION

Two-cover view at actual DSR (3PL 14d, excluding arrival/glitch days) vs projected DSR at 1.5x growth factor.

### Kits

| SKU | Stock | Projected DSR (1.5x) | Cover @ Projected | Actual DSR | Cover @ Actual |
|---|---|---|---|---|---|
| KIT-STA-2 | 2,387 | 31.5 | 76d | 14.9 | 160d |
| KIT-COM-4 | 3,606 | 61.5 | 59d | 29.1 | 124d |
| KIT-ULT-6 | 776 | 27.0 | 29d | 11.5 | 67d |

ULT-6 is tightest at 29d projected — but +2,660 inbound on held container. Fine once released.

### Liquids

| SKU | Stock | Projected DSR | Cover @ Proj | Actual DSR | Cover @ Actual | Flag |
|---|---|---|---|---|---|---|
| LIQ-HEA-5 (Heal) | 8,880 | 56.2 (kit-adj) | 158d | 56.2 | 158d | SAFE — just restocked |
| LIQ-BAS-2 (Base) | 1,575 | 16.5 | 95d | 11.0 | 143d | SAFE |
| LIQ-SEA-3 (Seal) | 1,191 | 13.2 | 90d | 8.8 | 135d | SAFE |
| LIQ-GLO-4 (Glow) | 1,620 | 9.6 | 169d | 6.4 | 254d | SAFE |
| LIQ-BON-1 (Bond) | 860 | 6.75 | 127d | 4.5 | 189d | SAFE |
| LIQ-SEN-2 (Low Odour Base) | 586 | 6.6 | 89d | 4.4 | 134d | SAFE |
| LIQ-SEN-4 (Low Odour Glow) | 440 | 5.4 | 81d | 3.6 | 123d | SAFE |
| LIQ-MAT-4 (Matte) | — | — | — | — | — | Not flagged |
| **LIQ-SOA-6 (Soak)** | **321** | **7.8** | **41d** | **5.2** | **62d** | **WARNING — +648 on held container** |

All liquids healthy at 1.5x. None stock out before CA 21062026 (5 Jul) even at model rate. Daniel's 16 Apr flag of Base/Seal/Soak/Bond/Remove Bowl at risk is **no longer true at 1.5x** — only Soak remains tight.

### Remove Products

| SKU | Stock | Projected DSR | Cover @ Proj | Actual DSR (3PL) | Cover @ Actual | Flag |
|---|---|---|---|---|---|---|
| ACC-REM (120ml) | 4,225 | 37.5 | 113d | 33.7 | 125d | SAFE |
| ACC-REM-500 (500ml) | 3,644 | ~18.0 | ~200d | 0* | 200d+ | SAFE — just restocked |
| ACC-REM-BOW (Bowl) | 1,341 | 90 (model inflated) | 15d | 14.4 | 93d | **Model DSR overstated** |

*ACC-REM-500 was OOS pre-check-in; post-restock demand to be measured in Sales Analysis.

**ACC-REM-BOW:** Model DSR shows 60/d → 1.5x = 90/d → 15d cover (model view). Actual 3PL deducts 14.4/d (bundle effect from ACC-REM-BUN-1 + BUN-2). Real cover 93d. **Greg still needs to correct model DSR from 60 to ~20.**

### Accessories / Inserts

| SKU | Stock | Actual Ded/d | Cover | Inbound | Note |
|---|---|---|---|---|---|
| ACC-INS (Instructions) | 13,723 | 49.9 | 275d | +10,080 held | SAFE |
| ACC-THA (Thank You) | 27,461 | 93.9 | 292d | +8,400 held | SAFE |
| ACC-LAB-CA (Booklet) | 9,039 | ~94 (ACC-THA proxy) | ~96d | None | New Mixam order needed ~mid-June |
| **ACC-NAI-WIP (Wipes)** | **38** | **1.3** | **29d** | **+836 held** | **WARNING — held container critical** |

### Packaging — CORRECTED (excl. paste glitches)

| SKU | Stock | True Ded/d | Cover | Inbound | Note |
|---|---|---|---|---|---|
| STO-BUB-BAG-L (Mailer) | 9,747 | ~55 | 177d | Zakka (unpaid, waiting) | SAFE |
| STO-MAI-2 (Small Box) | 10,710 | ~48 | 225d | +14,850 CA 21062026 | SAFE |
| STO-MAI-BAG-S (Satchel) | 10,670 | 44.5 | 240d | +15,000 CA 21062026 | SAFE |
| STO-BUB-BAG-S | 0 | 0 | — | 247 supplies their own | N/A |

---

## CONTAINER / ORDER STATUS

### CA 03022026 + CA 07042026 — HELD AT CUSTOMS (20d past ETA)
- **POS MODEL:** Status "On the Way", Est. Arrival 2 Apr 2026 (**stale — should read: Held**)
- **Reality:** Still held. Customs payment outstanding. Joel following up per user.
- **Growth factor:** 1.5x
- **Key contents (combined OL):**
  - Kits: STA +1,988, COM +4,788, ULT +2,660
  - ACC-REM-BOW +7,140, ACC-INS +10,080, ACC-THA +8,400
  - ACC-NAI-WIP +836 (critical — 38 on hand today)
  - LIQ-SOA-6 +648, LIQ-BON-1 +216
  - Colours: Blue Moon +200, Blush +200, Forest Muse +200, Icey +400, Sapphire +200, Violet Flush +200
- **Every day of customs delay tightens cover on ACC-NAI-WIP (29d) and LIQ-SOA-6 (62d) first.**

### CA Powder Room 24-03-2026
- **POS MODEL:** No dedicated block (small order, not tracked in header).
- **Reality:** Est. completion was 18 Apr with B113 jars. Slack 17 Apr ✅. Status unconfirmed — chase Lily.

### 31-01-2026 Swift Innovations Fill
- **POS MODEL:** Line removed (user confirmed).
- **Reality:** Delivered 21 Apr. Checked in 22 Apr: +7,500 Heal, +3,644 Remove 500ml.
- **Post-fill cover:** Heal 158d, Remove 500ml ~200d+.

### 04-03-2026 CA Print Order (Mixam labels)
- **POS MODEL:** Should show Delivered / closed; verify.
- **Reality:** 8,700 of 10,000 received (1,300 short). Mixam Canada not yet replied to 16 Apr claim (wrong Mixam replied 19-20 Apr).

### CA 21062026 (Birthday Sale)
- **POS MODEL:** Status "Ordering", Est. Completion 21 May 2026, Est. Arrival 5 Jul 2026, Growth factor 1.5x
- **Reality:** Deposit NOT paid. Sally waiting. Remy to reconfigure PO at 1.5x per Daniel's 22 Apr note before Joel places.
- **Contents (OL totals):** STA +1,036, COM +2,100, ULT +1,260 = 4,396 kits. Plus 15,000 STO-MAI-BAG-S, 14,850 STO-MAI-2, Birthday Sale replenishment colours.

### CA 25072026
- **POS MODEL:** Status "Ordering", Est. Completion 22 Jun 2026, Est. Arrival 6 Aug 2026, **Growth factor 2.0x (STALE — should be 1.5x)**
- **Reality:** Not yet placed. Fill PO place date 13 May.
- **ACTION:** Greg to update growth factor on CA 25072026 block from 2.0x to 1.5x. At 1.5x the contents will need re-sizing.

---

## STOCK-OUT FORECAST

### STOCKOUT BEFORE ARRIVAL (real risks only — glitches excluded)

| SKU | Stock | Actual DSR | Stocks Out | Next Inbound | Arrives | Gap |
|---|---|---|---|---|---|---|
| POW-BOR-355 (Bordeaux Nights) | 1 | 5.0 | OOS now | CA 25072026 +600 | 6 Aug | -106d |
| POW-RED-165 (Red Mischief) | 1 | 4.5 | OOS now | CA 25072026 +600 | 6 Aug | -106d |
| POW-GAR-656 (Garnet Games) | 9 | 4.3 | ~24 Apr | CA 25072026 +600 | 6 Aug | -104d |
| POW-ALL-146 (All Eyes On Me) | 39 | 3.0 | ~5 May | CA 25072026 +400 | 6 Aug | -93d |
| POW-INF-506 (Inferno Hour) | 42 | 3.0 | ~6 May | CA 25072026 +400 | 6 Aug | -92d |
| POW-SAF-149 (Saffron Blaze) | 50 | 2.4 | ~12 May | CA 25072026 +400 | 6 Aug | -86d |
| POW-VIO-11932 (Violet Flush) | 43 | 2.7 | ~9 May | CA 03022026 +200 (held) | TBD | Depends on customs |
| POW-ICE-ZGD16 (Icey) | 19 | 2.0 | ~1 May | CA 03022026 +400 (held) | TBD | Depends on customs |
| POW-GLA-CS02 (Glacier Glow) | 56 | 1.9 | ~21 May | CA 21062026 +800 | 5 Jul | -45d |
| POW-SAP-11933 (Sapphire Nights) | 65 | 1.9 | ~26 May | CA 03022026 +200 (held) | TBD | Depends on customs |
| POW-BLU-ZGD22 (Blue Moon) | 0 | 2.1 | OOS now | CA 03022026 +200 (held) | TBD | OOS until customs clears |

### NOTHING ON ORDER (new collection at risk)

| SKU | Stock | Actual DSR | Stocks Out | Note |
|---|---|---|---|---|
| **POW-BLO-042 (Blossom)** | **722** | ~18/d launch-rate | **~10 Jun** | **ZERO on any container — needs adding to CA 21062026 urgently** |
| POW-MOO-401 (Mood) | 1,080 | ~2.2 (glitch-corrected) | ~18 Aug | ZERO on any container — fine for now |
| POW-OPA-040 (Opal) | 739 | ~18 launch-rate | ~12 Jun | Only +200 on CA 25072026 (6 Aug) — gap |
| POW-ORC-038 (Orchid) | 702 | ~18 launch-rate | ~9 Jun | Only +200 on CA 25072026 (6 Aug) — gap |
| POW-RAD-043 (Radiant) | 715 | ~14 (post-glitch) | ~17 Jun | Only +200 on CA 25072026 (6 Aug) — gap |

**ACC-LAB-CA:** 9,039 units at ~94/d = 96d cover. No container inbound. Next Mixam order lead 14-21d → place by ~end June to stay ahead.

### SAFE
~200+ SKUs with 45d+ cover at actual DSR. Stock abundant relative to demand.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today)

- **Release CA 03022026 + CA 07042026 from customs.** 20 days past ETA. Single action restocks ACC-NAI-WIP (29d), LIQ-SOA-6 (62d), 6 colour SKUs + bulk kits / packaging / Remove Bowl.
- **Greg: fix CA 25072026 growth factor** — still 2.0x in header (should be 1.5x). At 2.0x the planned kit quantities overstate need.
- **Amend CA 21062026 to include POW-BLO-042 (Blossom).** 722 units, ~18/d launch demand, **zero on any container**, stocks out ~10 Jun. Before deposit is paid and PO locked.

### 🟡 WARNING (act this week)

- **Greg: paste glitches 11-16 Apr** distort DSR calcs for POW-MOO-401, POW-RAD-043, STO-MAI-2, STO-BUB-BAG-L. Re-paste those days or manually correct.
- **Greg: correct ACC-REM-BOW model DSR from 60 to ~20/d** (pending from 15 Apr).
- **Reconfigure CA 21062026 PO at 1.5x growth factor** before Joel places deposit (Daniel's 22 Apr note).
- **Consider CA 21062026 top-up** for new collection with no/insufficient inbound: Opal, Orchid, Radiant (only +200 on CA 25072026 — Aug).
- **ACC-LAB-CA next Mixam order** — plan for ~end June placement. Also chase 1,300 unit shortfall from current order.
- **Follow up Mixam Canada** — no reply yet on shortfall claim (emailed 16 Apr, wrong Mixam replied 19-20 Apr).

### 🟢 MONITOR (FYI)

- Swift fill fully checked in — Heal 158d cover, Remove 500ml ~200d. No next fill needed for months.
- Zakka bubble mailers — Vanessa in contact, paying when ready. 177d cover, no urgency.
- Acetone refund from Univar — Joel to confirm received.
- CA Powder Room completion — chase Lily.

---

## LOCAL FILL FORECAST

### Swift Innovations — Heal + Remove 500ml
- Post-fill stock: Heal 8,880 at 56.2/d (kit-adj) → **158d cover**
- Post-fill stock: Remove 500ml 3,644 at ~18/d pre-OOS → **~200d cover**
- Lead time: ~28d from all ingredients at Swift.
- **Next fill place date: ~mid-August** (when Heal drops to ~60d target) — on hold per Joel (9 Apr). No urgency.

---

## PO RECOMMENDATIONS

Target 14-21d lean kit cover. No kits require PO action now — held container restocks STA to 180d+ / COM to 150d+ / ULT to 100d+ cover at actual DSR once released.

### Flagged for imminent PO deadlines

| SKU | Stock | Cover | Next PO By | Raw Goods By | Status |
|---|---|---|---|---|---|
| POW-BLO-042 | 722 | ~40d | — (add to CA 21062026) | — | **🔴 Container amendment needed** |
| ACC-LAB-CA | 9,039 | ~96d | Mixam ~end June | n/a (local print) | 🟢 On track |

No CN raw goods POs required at this stage — kit cover is long.

---

## CASCADING ARRIVAL PROJECTION

Actual kit DSR 55.5/d (STA 14.9 + COM 29.1 + ULT 11.5).

| Stage | Kit Stock | Cover @ Actual 55.5/d | Cover @ Projected 120/d |
|---|---|---|---|
| NOW | 6,769 | 122d | 56d |
| + CA 03022026/07042026 (if released ~27 Apr, +9,436 kits) | ~16,000 | 288d | 133d |
| + CA 21062026 (5 Jul, +4,396 kits) | ~17,000 (after 70d consumption) | 306d | 142d |
| + CA 25072026 (6 Aug, +5,404 kits) | ~20,000 (after 32d) | 360d | 167d |

**Overstock flag:** At actual selling rates, kit cover approaches 12 months post-CA 25072026 arrival. Even at 1.5x projected, post-CA 25072026 sits at 167d (target 45-75d). **CA 25072026 kit quantities should be reviewed.** Suggest reducing STA/COM/ULT OL by 40-50% to land closer to target cover.

### If CA 03022026 + CA 07042026 is delayed another 3 weeks (customs drags)

- ACC-NAI-WIP: 38 at 1.3/d → 29d → OOS ~21 May
- LIQ-SOA-6: 321 at 5.2/d → 62d → OOS ~23 Jun (before CA 21062026 5 Jul — 12d gap)
- ACC-REM-BOW at actual 14.4/d: 93d cover — safe
- All kits still safe at actual rate.
- Held colours (Icey, Violet Flush, Sapphire, Blue Moon, Blush, Forest Muse) all stocked out well before next container arrives.

---

## FOLLOW-UP ITEMS

### Immediate
- [ ] Joel: release CA 03022026 + CA 07042026 from customs (20d overdue)
- [ ] Greg: fix CA 25072026 growth factor 2.0x → 1.5x
- [ ] Daniel/Remy: add POW-BLO-042 Blossom to CA 21062026 before deposit paid

### By End of Week
- [ ] Greg: re-paste 11 Apr (POW-MOO/RAD + multi-SKU), 13 Apr (STO-MAI-2), 15-16 Apr (STO-BUB-BAG-L)
- [ ] Greg: correct ACC-REM-BOW model DSR 60/d → 20/d
- [ ] Remy: reconfigure CA 21062026 PO at 1.5x before Joel pays deposit
- [ ] Remy: follow up Mixam Canada on 1,300-unit shortfall (no reply since 20 Apr)
- [ ] Consider topping up Opal / Orchid / Radiant on CA 21062026

### Ongoing
- [ ] Monitor customs release and 247 check-in when released (~3-5d after release)
- [ ] Track ACC-LAB-CA deduction rate for next Mixam order timing (~end June)
- [ ] Powder Room container completion — chase Lily
