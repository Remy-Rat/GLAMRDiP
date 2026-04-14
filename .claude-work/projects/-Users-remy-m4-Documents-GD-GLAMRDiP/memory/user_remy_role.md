---
name: Remy's role and daily workflow
description: Remy's inventory management responsibilities and daily review process — informs how to structure skill outputs
type: user
---

Remy Verrocchi — Inventory & Supply Chain Management at Scale Labs for GLAMRDiP.

**Daily workflow:**
1. Shopify store check, WeChat, Notion, Emails
2. Region review (Mon=AUS, Tue=UK, Wed=CA, Thu=Nordic, Fri=FR/SP)
3. For each region review:
   - Check website for OOS
   - Check latest Shopify & 3PL data
   - Confirm Sally PO Tracker & Lily Shipment Tracker against POS MODEL (not yet connected to Claude)
   - Review SALES sheet (surges, drops, large deductions)
   - Review stock at each container in POS MODEL — container by container, projecting what stocks out and when
   - B2G4 batch expiry check
   - Local liquids fill status
   - Write Slack summary with: container status, OOS, could-go-OOS, problems, sell rate
   - Review next local liquid fill date
4. PO Procedure: verify review → create recommended order → send for review

**Key mental model:** Container-by-container stock-out forecasting. "At current sell rate, X stocks out in Y days. The container arrives in Z days. Gap = Y-Z days of stockout." This is the core value of the daily review — identifying gaps before they happen.

**Data sources not yet connected:** Sally PO Tracker, Lily Shipment Tracker, Shopify admin (live OOS check). Lead times needed to enable automated forecasting.
