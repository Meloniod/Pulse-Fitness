# PULSE — Personal Trainer Management Platform

PULSE is a client-demonstration MVP for independent personal trainers delivering in-person and online coaching. It includes a responsive Next.js demo and a reproducible companion workbook.

## Product scope
- Client register: create, search and archive
- Training programme planning and assignment
- Session scheduling and completion tracking
- Nutrition logging: client-reported calories, protein and hydration
- Basic manual payment tracking
- Dashboard and performance summary

## Run the demo
Requires Node.js 20+.

```bash
npm install
npm run dev
```

Open http://localhost:3000.

## Repository map
- `src/app/` — Next.js App Router application
- `tracker/` — Google Sheets-compatible CSV templates and workbook instructions
- `scripts/build_tracker.py` — generates the 11-tab XLSX companion tracker
- `docs/` — product brief, requirements, architecture, decisions, user guide, demo script, QA checklist, roadmap, limitations and handover index
- `assets/` — temporary brand guide and client demo checklist
- `.github/workflows/ci.yml` — Next.js build and workbook generation

## Generate the companion workbook
Requires Python 3.10+.

```bash
pip install openpyxl
python scripts/build_tracker.py
```

The workbook is generated at `tracker/PULSE_Personal_Trainer_Tracker.xlsx`. GitHub Actions also uploads it as a workflow artifact after a successful tracker build.

## Demo data and privacy
The demo uses fictional sample records and browser `localStorage`. Data stays in the current browser and does not sync across devices. There is no authentication, production database, tenant isolation, client portal, automated messaging or payment processing. Do not enter real client, health, nutrition or payment-card information.

## Production direction
See `docs/PRODUCTION_ROADMAP.md` for the staged move to Supabase/PostgreSQL, authentication, row-level security, server-side validation, audit logging, backups, monitoring, consent and privacy controls, and deployment.

## Release status
The repository now contains the application source, project documentation, tracker templates and workbook generator. A successful production build and browser QA still need to be confirmed by CI and the manual checks in `docs/QA_CHECKLIST.md` before describing this as release-ready.
