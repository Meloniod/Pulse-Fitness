# Production Roadmap

This roadmap is a proposed next phase, not a claim that these capabilities already exist.

## Phase 0 — Validate the demo
- Complete install, production build and browser QA.
- Validate workflows with 3–5 independent trainers.
- Record feedback and prioritise the most frequent administrative pain points.
- Confirm data fields, roles, reports and client portal requirements.

## Phase 1 — Secure foundation
- Provision Supabase project and environments.
- Implement Supabase Auth.
- Design PostgreSQL schema and migrations.
- Add tenant and membership model.
- Enforce RLS policies and test cross-tenant isolation.
- Add server-side Zod validation.
- Add audit logging for sensitive operations.

## Phase 2 — Core workflows
- Replace localStorage with server-side persistence.
- Implement client, programme, session, nutrition and payment repositories.
- Add pagination, filtering and robust empty/error states.
- Add import/export and data backup processes.

## Phase 3 — Business operations
- Add invoicing and payment provider integration only after provider, reconciliation and compliance decisions.
- Add notifications and calendar integration.
- Add configurable reporting.
- Add trainer availability and cancellation rules.

## Phase 4 — Client experience
- Add optional client portal.
- Add client consent and profile management.
- Add progress sharing with trainer-controlled permissions.
- Add secure messaging only if validated.

## Release readiness
- Privacy impact and data-flow review.
- Applicable POPIA and other legal review.
- Penetration/security testing.
- Backup restore test.
- Monitoring and incident response.
- Terms, privacy notice, retention and deletion processes.
- Accessibility and performance review.
- Staged deployment and rollback plan.
