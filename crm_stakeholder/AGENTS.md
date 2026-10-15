# crm_stakeholder

## Purpose

Stakeholders on leads/opportunities: a partner with a role (shared
`project.stakeholder.role`) and a note per lead; the partner form shows the
leads/opportunities in which the partner is a stakeholder.

## Models

- `crm.stakeholder`: `role_id` (required, restrict), `partner_id` (required, cascade),
  `lead_id` (required, cascade), `note`.
- `crm.lead.stakeholder_ids`, `res.partner.lead_stakeholder_ids` (One2many).

## Rules

- Sales managers: full access, salesmen: no delete; stakeholder roles are readable for
  salesmen and managed by sales managers (menu CRM > Configuration > Stakeholder Roles).

## Pitfalls

- Origin: Weboffice module from the Cosin repository (OPL-1), relicensed to AGPL-3 for
  OCA by its author (2026-10-02).
- Depends on `project_stakeholder` (not merged in OCA 19.0, PR project#1783).
- There is no `crm.stakeholder.role` anymore (removed in 19.0, roles come from
  project_stakeholder).
- Customer views (e.g. woa_cosin_stakeholder) replace the partner page via
  `//page[field[@name='lead_stakeholder_ids']]`; keep the field name and page structure.
