# Architecture

## Demo architecture
- Next.js App Router
- React client-side workspace
- TypeScript
- Tailwind CSS
- Lucide icons
- Browser localStorage persistence
- Fictional seed data

## Demo data domains
- Client
- Programme
- Session
- Nutrition entry
- Payment record

## State and persistence
The demonstration stores a serialised application state in browser localStorage. This is intentionally a single-browser simulation. It is not a secure or shared data store.

## Production target architecture
- Next.js App Router UI and server actions/route handlers
- Supabase Auth for trainer identity
- PostgreSQL for tenant-scoped records
- Row Level Security (RLS) on every tenant-owned table
- Zod validation at server boundaries
- Supabase Storage only for explicitly required documents
- Audit events for sensitive record access and mutations
- Scheduled backups, monitoring and error reporting

## Data ownership
Every production record must be associated with a trainer or organisation tenant. Authorization must be checked server-side; hiding UI elements is not authorization.

## Sensitive data
Fitness assessments and nutrition records can reveal personal information. Collect the minimum necessary, document purpose and consent, restrict access, define retention, and support correction/deletion processes. Do not store payment-card data.
