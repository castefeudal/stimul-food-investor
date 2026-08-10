# STIMUL FOOD Investor - implementation report

The investor landing page was rebuilt as an interactive investment memo/dashboard with product evidence, source-aware economics, scenario tools and a safer document-delivery architecture.

## Investor UX and analytics
- Hero KPI dashboard tied to the model snapshot.
- Investment-thesis causal chain from problem to validation and scale decision.
- Product-evidence section and full 14-day public menu explorer.
- Bottom-up market/active-customer calculator.
- Editable unit-economics calculator with visible cost stack and break-even.
- Volume sensitivity chart and conservative/base/upside sensitivity cases.
- 36-month checkpoint table and first-13-week cash view.
- CAC/contribution-LTV scenario calculator.
- Use-of-funds mapping, milestone gates and risk register.

## Financial source of truth
Current snapshot: average price 44.35 BYN; stable variable cost 30.2098 BYN/ration-day; stable contribution 14.1402 BYN/ration-day; stable contribution margin 31.88%; break-even ~32.65 ration-days/day before advertising; requested funding 68,000 BYN.

## Data-room/security
- Removed ineffective `confirm() + sessionStorage` protection.
- Confidential PDF/XLSX stay outside public repo/deployment.
- Document CTA defaults to request flow; protected entry can be configured separately.
- `noindex` is explicitly not access control.

## Data requiring confirmation
Actual kitchen/supplier/packaging/delivery quotes; tax/legal treatment; real paid-pilot CAC/repeat/waste/on-time data; secure data-room provider; final legal/privacy operator details.
