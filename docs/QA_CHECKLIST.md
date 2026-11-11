# QA Checklist

Run these checks before a client-facing demonstration.

## Setup
- [ ] Node.js 20+ installed
- [ ] `npm install` completes successfully
- [ ] `npm run build` completes successfully
- [ ] `npm run dev` starts without runtime errors

## Core workflows
- [ ] Dashboard loads with fictional seed data
- [ ] Add a client; verify it appears in the register
- [ ] Search by client name and email
- [ ] Archive a client
- [ ] Create and assign a programme
- [ ] Create a session
- [ ] Mark a session completed
- [ ] Log nutrition values
- [ ] Record a payment
- [ ] Mark a payment paid
- [ ] Refresh the page; verify local persistence
- [ ] Reset; verify original seed data returns

## Responsive and usability
- [ ] Desktop layout
- [ ] Tablet layout
- [ ] Mobile layout
- [ ] Dialogs and forms remain usable on small screens
- [ ] Tables can be reviewed on narrow screens
- [ ] Empty states and validation errors are understandable

## Privacy and demo hygiene
- [ ] Demo label is visible
- [ ] No real client data is present
- [ ] No secrets are committed
- [ ] Explain local-only storage and lack of authentication
- [ ] Explain that payments are not processed

## Tracker
- [ ] Open workbook in Excel
- [ ] Import a copy into Google Sheets
- [ ] Check formulas and dropdown validations after import
- [ ] Test one sample client, programme, session, nutrition entry and payment
