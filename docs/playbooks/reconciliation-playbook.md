# Reconciliation & Financial Controls Playbook

## Objective
Validate that payment transactions remain accurate and traceable from source initiation through downstream settlement and reporting.

## Reconciliation Controls
| Control | Description |
|---|---|
| Transaction Count Match | Source, processor, settlement, and reporting counts match |
| Amount Match | Debit, credit, fee, and settlement amounts reconcile |
| Status Match | Transaction statuses remain consistent across platforms |
| Duplicate Detection | Duplicate payment or settlement records are identified |
| Exception Review | Failed, rejected, or reversed transactions are tracked |
| Audit Evidence | SQL extracts and dashboards support release signoff |

## SQL Evidence
See `sql/reconciliation/payment_reconciliation.sql`.
