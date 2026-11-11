# Product Requirements

## Functional requirements

| ID | Requirement | MVP acceptance |
|---|---|---|
| FR-01 | Client register | Add, search and archive client records |
| FR-02 | Programme planning | Create a programme and assign it to a client |
| FR-03 | Session scheduling | Create a session with client, date, time and type |
| FR-04 | Session outcomes | Mark scheduled sessions completed |
| FR-05 | Nutrition logging | Record client, meal, calories, protein, hydration and date |
| FR-06 | Payment tracking | Record amount/date/status and mark a payment paid |
| FR-07 | Dashboard | Show active clients, sessions, revenue received and outstanding amount |
| FR-08 | Performance | Summarise session outcomes and logged activity |
| FR-09 | Persistence | Retain demo changes in the current browser |
| FR-10 | Reset | Restore fictional seed data |

## Non-functional requirements
- Responsive layout for desktop, tablet and mobile.
- Clear navigation and readable data tables.
- No secrets embedded in client-side code.
- Demo must clearly identify itself as a demonstration.
- Use fictional sample data only.
- Production implementation must enforce server-side authorization and tenant isolation.

## Out of scope
Authentication, client self-service portal, multi-trainer organisations, automated messaging, recurring billing, payment gateway integration, wearables, medical advice and automated diet prescription.
