# PULSE — Personal Trainer Management Platform

PULSE is a client-demonstration MVP for independent personal trainers delivering in-person and online coaching. It includes a responsive Next.js demo and a companion Google Sheets-compatible workbook.

## Product scope
- Client register and client lifecycle management
- Training programme planning and assignment
- Session scheduling and completion tracking
- Nutrition logging (client-reported calories, protein and hydration)
- Basic payment register and payment status tracking
- Dashboard and performance overview

## Repository contents
- `app/` — Next.js application source
- `tracker/` — Excel workbook compatible with Google Sheets import
- `docs/` — product brief, requirements, architecture, user guide, demo script, QA checklist, production roadmap and known limitations
- `assets/` — brand identity notes and presentation collateral

## Demo setup
Requires Node.js 20+.

```bash
npm install
npm run dev
```

Open `http://localhost:3000`.

## Demo data and privacy
The demo uses fictional sample records and browser `localStorage`. It is not a production system. Do not enter real client, health, payment-card or other sensitive information. There is no authentication, server-side persistence, tenant isolation, payment processing or client portal.

## Production direction
See `docs/PRODUCTION_ROADMAP.md` for the staged migration to Supabase/PostgreSQL, authentication, tenant isolation with RLS, server-side validation, audit logging, backups, monitoring, consent and privacy controls, and deployment.

## Project status
The source and workbook are supplied for client demonstration and further development. A successful production build and browser QA have not yet been verified in this environment; run the checks in `docs/QA_CHECKLIST.md` before presenting it as release-ready.
