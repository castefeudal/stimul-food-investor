# STIMUL FOOD — investor digital data room

Interactive investor memo based on the provided business plan and financial model.

## Architecture

- `src/data/investor.json` — investor assumptions and scenarios extracted from the provided financial model.
- `public-data/menu.public.json.gz.b64` — compressed sanitized product snapshot restored by `build.py`.
- `src/assets/investor.js` — unit economics calculator, volume sensitivity, market math, funding and scenarios.
- `private-docs/` — confidential PDF/XLSX source materials. **Never deployed or committed to this public repository.**
- `dist/` — generated static investor site, intentionally without PDF/XLSX files.

## Security model

The previous `confirm() + sessionStorage` pattern did not protect static files. It has been removed. Document buttons create an addressable request in the contact form. For protected data-room access use authenticated private storage/signed URLs and configure `secureDataRoomUrl`.

## Run locally

```bash
python build.py
cd dist
python -m http.server 8001
```

## Financial source of truth

The V20 dashboard uses the six-program weighted 5-day mix: ASP 47.1614 BYN; stable weighted food 14.67432; kitchen 5.50; packaging 3.20; delivery 2.80; other variable 1.50; waste 3% of food; payment fee 1.8%; tax scenario 6%; fixed mature costs 12,000 BYN/month; 26 working days; stable contribution 15.3683 BYN and 32.59%; break-even without marketing ~30.03 ration-days/day. Interactive edits are scenarios, not forecasts.

## Activation boundary

- Confirm kitchen, packaging and supplier quotes.
- Confirm tax/legal treatment with accountant/legal counsel.
- Connect protected data room.
- Add real pilot results (CAC, repeat, waste, on-time delivery) when measured.

## Critical hosting note

`noindex` is not access control. The public GitHub Pages workflow deploys only sanitized `dist/`; `private-docs/` and `private-data/` are gitignored and excluded. If investor assumptions themselves become confidential, move repository/hosting behind access control.
