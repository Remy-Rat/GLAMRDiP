# POS MODEL CHECK — Nordic — 14 Apr 2026

> **Running without 3PL daily data.** B360 tab is empty (`#REF!`). No deduction analysis, no container arrival detection, no Shopify-3PL alignment check. All stock figures from POS MODEL only.

## DATA FRESHNESS

- **POS MODEL last updated:** 14 Apr 2026
- **3PL data (B360 tab):** EMPTY — no daily stock snapshots available
- **Shopify:** 13 Apr 2026 (4 stores: DK, NO, SE, FI combined)
- **Growth factor:** 0.7x (76 base → 53.2 scaled)
- **Kit DSRs (model base):** STA 22 | COM 22 | ULT 32 (total 76/day)
- **Vessels:** 45 days to Nordic
- **Dual stock:** D- prefix = Dippi, non-prefix = GLAMRDiP. Both used to fulfil orders.

---

## STOCK POSITION — COMBINED (Dippi + GLAMRDiP)

### Kits

| Kit | D- Stock | GD Stock | Combined | GD 14d DSR | Combined Cover |
|---|---:|---:|---:|---:|---:|
| Starter (KIT-STA-2) | 1 | 1,827 | 1,828 | 8.8/d | **208d** |
| Complete (KIT-COM-4) | 6 | 1,839 | 1,845 | 11.5/d | **160d** |
| Ultimate (KIT-ULT-6) | 3 | 2,615 | 2,618 | 16.9/d | **155d** |

Kits are very healthy. Dippi kits essentially zero (being returned/cancelled — negative D- DSR indicates refunds). NORDIC 14012026 container clearly arrived and was checked in — GLAMRDiP kit stock matches expected quantities.

### Liquids

| SKU | Product | D- Stock | GD Stock | Combined | Comb DSR | Cover | Flag |
|---|---|---:|---:|---:|---:|---:|---|
| LIQ-HEA-5 | Heal | 1,722 | 0 | 1,722 | 37.3/d (kit-adj) | **46d** | WATCH |
| LIQ-BAS-2 | Base | 0 | 581 | 581 | 17.0/d | **34d** | WARNING |
| LIQ-SEN-2 | Sensitive Base | 0 | 143 | 143 | 3.6/d | 40d | WATCH |
| LIQ-SEA-3 | Seal | 322 | 427 | 749 | 14.3/d | 52d | OK |
| LIQ-GLO-4 | Glow | 980 | 427 | 1,407 | 9.9/d | 142d | OK |
| LIQ-SEN-4 | Sensitive Glow | 0 | 164 | 164 | 2.6/d | 63d | OK |
| LIQ-BON-1 | Bond | 0 | 567 | 567 | 5.2/d | 109d | OK |
| LIQ-MAT-4 | Matte | 13 | 215 | 228 | 5.0/d | 46d | WATCH |
| LIQ-SOA-6 | Soak | 68 | 427 | 495 | 4.4/d | 112d | OK |

- **Heal has no GLAMRDiP stock** — all 1,722 is Dippi. Being used for GLAMRDiP kits at 3PL (kit-adjusted 37.3/d). 46d cover. No local filler set up in Nordic.
- **Base at 34d cover.** Only GLAMRDiP stock (581). Not kit-adjusted in Nordic (pre-packed in CN kits). Selling 17.0/d standalone. No Dippi Base stock visible (Dippi used different name "Build"?).

### Remove Products — CRITICAL

| SKU | Product | D- Stock | GD Stock | Combined | Comb DSR | Cover | Flag |
|---|---|---:|---:|---:|---:|---:|---|
| ACC-REM | Remove 120ml | 29 | 0 | 29 | 8.9/d | **3d** | **CRITICAL** |
| ACC-REM-500 | Remove 500ml | 559 | 0 | 559 | 21.6/d | **26d** | WARNING |
| ACC-REM-BOW | Remove Bowl | 879 | 2,578 | 3,457 | 5.4/d | 640d | OK |

- **ACC-REM (Remove 120ml) is effectively OOS.** 29 units at 8.9/day = 3 days. Only Dippi stock remains, no GLAMRDiP stock. This is a live stockout — customers ordering Remove 120ml will be backordered within days.
- **ACC-REM-500 at 26d.** Only Dippi stock (559 units). No GLAMRDiP stock. Will stock out mid-May.

### Packaging & Inserts

| SKU                       | D- Stock | GD Stock | Notes                                                         |
| ------------------------- | -------: | -------: | ------------------------------------------------------------- |
| D-BUBBLE_MAILER_BAG       |    7,102 |        — | Dippi branded                                                 |
| STO-BUB-BAG-L             |        — |   38,864 | GLAMRDiP bubble mailers — massive stock                       |
| D-SMALLER_MAILER_BAG      |    3,070 |        — | Dippi                                                         |
| STO-MAI-BAG-S             |        — |    4,944 |                                                               |
| STO-MAI-2                 |        — |    5,521 |                                                               |
| D-INSTRUCTION_SE/NO/DK/FI |   varies |        — | Dippi language inserts (SE:4,519, NO:382, DK:1,173, FI:2,773) |
| D-THANKYOUCARD_SE/FI      |   varies |        — | Dippi (SE:3,367, FI:1,873). NO and DK missing                 |
| ACC-LAB-*                 |        — |        — | **NOT TRACKED in POS MODEL**                                  |

- **D-INSTRUCTION_NO (Norwegian instructions): 382 units.** At ~14 orders/day to Norway, this is ~27d cover. Lowest of the 4 languages.
- **D-THANKYOUCARD_NO and DK: 0 units.** Norwegian and Danish thank you cards are OOS. Were they printed by Adib?
- **GLAMRDiP inserts not in POS MODEL.** Adib's locally-printed GLAMRDiP inserts are not tracked here. Unknown stock level.
- **Labels booklets (ACC-LAB) not tracked at all.** Need Adib/Axel to confirm stock.

### Colours — Key Findings

| Finding | Detail |
|---|---|
| **POW-WAV-SU017 (Wavvy): 10,000 units** | **STOCK ERROR still uncorrected.** Should be 200. Axel confirmed likely 200 on 12 Mar, created work order. Never completed. |
| GLAMRDiP Clear | 6,139 — healthy, #1 colour at 41.9/d = 146d |
| Dippi Clear | 1,297 — still being consumed (8.5/d D- sales) |
| Total combined colour stock | ~160,000+ units across D- and GD |
| 9 colours with 0 GD stock | These are Dippi-only — being sold through via clearance |

---

## CONTAINER / ORDER STATUS

### NORDIC 25122025 (Delivered)
- **POS MODEL:** Delivered, Est. Arrival 5 Dec 2025
- **Reality:** Delivered. GLAMRDiP stock checked in. This is the stock showing in the GD columns.

### NORDIC 14012026
- **POS MODEL:** No shipment block found in model (references not filled in)
- **Reality:** Est. arrival was 24 Mar. GLAMRDiP kit stock (STA 1,827, COM 1,839, ULT 2,615) confirms it arrived. Liquid and accessory quantities also match expected.
- **Status:** Arrived and checked in. Not reflected in POS MODEL shipment blocks.

### NORDIC 01072026 (In Production — per user)
- **POS MODEL:** Not reflected. No shipment block with dates.
- **Reality:** User confirmed "in production now" (14 Apr).
- **Est. arrival:** Unknown. If completion ~mid-May + 45d vessel = ~early July?
- ACTION: Greg to add this to POS MODEL with dates. Daniel to confirm Est. Completion and Est. Arrival.

### NORDIC 03062026
- **POS MODEL:** Not reflected.
- **Reality:** Was planned for placement 28 Mar. No evidence it was placed. Greg said "still in planning stage" on 23 Mar for 01072026. 03062026 status completely unknown.
- ACTION: Daniel/Joel to confirm whether this was placed, merged into 01072026, or cancelled.

---

## STOCK-OUT FORECAST

### CRITICAL — Stocking out NOW

| SKU | Stock | DSR | Stocks Out | Inbound | Action |
|---|---:|---:|---|---|---|
| ACC-REM | 29 | 8.9/d | **~17 Apr (3 days)** | Nothing confirmed | **OOS imminent.** No GLAMRDiP stock exists. Must be on NORDIC 01072026 or sourced locally. |

### WARNING — Stocks out before likely container arrival (~early July)

| SKU | Stock | DSR | Stocks Out | Gap to Container |
|---|---:|---:|---|---|
| ACC-REM-500 | 559 | 21.6/d | ~10 May | ~55d gap |
| LIQ-BAS-2 | 581 | 17.0/d | ~18 May | ~45d gap |
| LIQ-SEN-2 | 143 | 3.6/d | ~24 May | ~35d gap |
| LIQ-HEA-5 | 1,722 | 37.3/d (kit-adj) | ~29 May | ~30d gap |
| D-INSTRUCTION_NO | 382 | ~14/d | ~11 May | ~50d gap |

Note: Container arrival estimated "early July" for NORDIC 01072026. If it's sooner, gaps narrow. But with no confirmed dates, these are best guesses.

### WATCH

| SKU | Stock | DSR | Cover |
|---|---:|---:|---:|
| LIQ-MAT-4 | 228 | 5.0/d | 46d |
| LIQ-SEN-4 | 164 | 2.6/d | 63d |

### SAFE

- All kits: 155-208d cover
- Most colours: 50-200d+ cover (massive from NORDIC 14012026 + NORDIC 25122025)
- Bond, Seal, Glow, Soak: 50-142d
- Remove Bowl: 640d

---

## WHAT NEEDS ACTION

### CRITICAL (act today)

- **ACC-REM (Remove 120ml): 3 days cover.** 29 units at 8.9/d. Effectively OOS. No GLAMRDiP stock exists. Check if NORDIC 01072026 includes Remove 120ml. If not, must source — there are no local fillers in Nordic.
- **POS MODEL is not maintained for Nordic GLAMRDiP.** No DSR, no days cover, no shipment blocks for recent/upcoming containers. Greg needs to set this up or the model is useless for forecasting.

### WARNING (act this week)

- **ACC-REM-500 (Remove 500ml): 26d cover.** 559 units (all Dippi). No GLAMRDiP stock. Stocks out ~10 May. No local filler. Must be on next container.
- **LIQ-BAS-2 (Base): 34d cover.** 581 units at 17.0/d. Stocks out ~18 May. No local filler for Base in Nordic (planned but not set up).
- **LIQ-HEA-5 (Heal): 46d at kit-adjusted rate.** 1,722 units (all Dippi). Used for both D- and GD kit fulfilment. No local filler. Stocks out ~29 May.
- **D-INSTRUCTION_NO (Norwegian instructions): 27d.** Adib may have printed more — confirm.
- **D-THANKYOUCARD_NO and DK: 0 units.** OOS. Were these printed?
- **NORDIC 03062026 status: UNKNOWN.** Was it placed? Merged? Cancelled?
- **POW-WAV-SU017: 10,000 error.** 5 weeks since work order created, still uncorrected. Chase Axel.

### MONITOR

- **Demand dropped significantly post-transition.** 35.5 kits/day (14d) vs 76/day model = 0.47x actual growth factor. Weekly trend shows W14-W16 at 17-21/d — this may be a temporary dip (transition disruption) or a new baseline.
- **Dippi clearance is slow.** D- SKUs still selling but at declining rates. Many colours have hundreds of units that may sit for months.

---

## POS MODEL GAPS — Nordic-Specific

The Nordic POS MODEL has critical gaps that don't exist in other regions:

1. **No DSR or days cover for GLAMRDiP SKUs.** The model only calculates these for D- SKUs. GLAMRDiP is now the primary brand.
2. **No shipment blocks for NORDIC 14012026 or NORDIC 01072026.** Container references, dates, and OL quantities are not filled in.
3. **B360 tab is empty.** No daily stock snapshots from Shelfless/Bring.
4. **POW-WAV-SU017 stock error (10,000 → 200) uncorrected.**
5. **Inserts tracked under D- names only** (D-INSTRUCTION_SE etc). GLAMRDiP inserts not in model.
6. **ACC-LAB not tracked at all** for Nordic.

Until these are fixed, the POS MODEL cannot be used for Nordic forecasting. All analysis in this check uses Shopify + POS MODEL stock counts manually.
