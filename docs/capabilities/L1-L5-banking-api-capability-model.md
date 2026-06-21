# L1–L5 Banking API Quality Engineering Capability Model

## L1 – API Smoke & Availability
Verifies API availability, baseline response, and required-field handling.
Evidence: `tests/l1_smoke/test_api_smoke.py`

## L2 – Contract, Schema & Message Validation
Verifies JSON contract rules and ISO 20022-style XML/XSD structure.
Evidence: `tests/l2_contract/`, `schemas/json/`, `schemas/xml/`

## L3 – Banking Workflow & Service Orchestration
Verifies payment initiation, posting, settlement, and status inquiry.
Evidence: `tests/l3_workflow/test_payment_lifecycle.py`

## L4 – Reconciliation & Financial Controls
Verifies source, settlement, and reporting consistency using SQL controls.
Evidence: `tests/l4_reconciliation/`, `sql/reconciliation/`

## L5 – Release Governance & Executive Quality Gates
Verifies release readiness score and Go/No-Go gate logic.
Evidence: `tests/l5_governance/test_release_governance_gate.py`
