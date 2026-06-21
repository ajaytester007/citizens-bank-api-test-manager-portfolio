# Citizens Bank API Test Manager Portfolio – Enhanced Functional Version

Runnable Banking API Quality Engineering solution aligned to API Test Manager / ReadyAPI / Banking Payments roles.

## L1–L5 Capability Coverage

| Level | Capability | Functional Evidence |
|---|---|---|
| L1 | API Smoke & Availability | Health check, required-field rejection |
| L2 | Contract & Schema Validation | JSON Schema validation, ISO 20022-style XML/XSD validation |
| L3 | Banking Workflow Validation | Payment initiation → posting → settlement → status inquiry |
| L4 | Reconciliation & Financial Controls | SQLite SQL controls for source vs settlement vs reporting |
| L5 | Release Governance | Release-readiness score and Go/No-Go quality gate |

## Run Locally

```bash
pip install -r requirements.txt
pytest -q
```

## Tools Represented

ReadyAPI/SOAPUI design, Postman collection, Pytest, JSON Schema, XML/XSD, SQL reconciliation, GitHub Actions, CI/CD quality gates, release governance.
