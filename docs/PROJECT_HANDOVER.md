# PULSE — Project Handover Index

## Repository map
- Root README — project overview and local setup.
- src/app — Next.js application.
- docs/PRODUCT_BRIEF.md — audience, problem, value proposition and MVP scope.
- docs/REQUIREMENTS.md — functional and non-functional requirements.
- docs/ARCHITECTURE.md — demo and production architecture.
- docs/DECISIONS_AND_ASSUMPTIONS.md — approved discovery decisions and open assumptions.
- docs/USER_GUIDE.md — trainer-facing operating instructions.
- docs/CLIENT_DEMO_SCRIPT.md — suggested 8–10 minute walkthrough.
- docs/QA_CHECKLIST.md — manual release and workflow checks.
- docs/PRODUCTION_ROADMAP.md — staged production plan.
- docs/KNOWN_LIMITATIONS.md — explicit demo constraints.
- assets/BRAND_GUIDE.md — temporary visual identity.
- tracker/ — workbook instructions and CSV templates.
- scripts/build_tracker.py — creates the 11-tab XLSX tracker.
- .github/workflows/ci.yml — Next.js build and tracker generation workflow.

## Current delivery scope
PULSE is a demonstration for independent personal trainers delivering in-person and online coaching. It includes client records, programme planning, session scheduling, client-reported nutrition logging, manual payment status tracking and a dashboard.

## Rebuild the companion workbook
Install Python 3.10+ and openpyxl, then run:

    pip install openpyxl
    python scripts/build_tracker.py

The generated workbook is saved to tracker/PULSE_Personal_Trainer_Tracker.xlsx. The GitHub Actions workflow also publishes it as a workflow artifact after a successful tracker job.

## Important release gate
Do not represent this project as production-ready until the build and manual QA checklist pass. Demo data is stored in browser localStorage only. There is no authentication, multi-user sync, secure backend or payment processing.
