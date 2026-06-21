# How to Run Locally

```bash
pip install -r requirements.txt
pytest -q
```

Run by level:

```bash
pytest -q tests/l1_smoke
pytest -q tests/l2_contract
pytest -q tests/l3_workflow
pytest -q tests/l4_reconciliation
pytest -q tests/l5_governance
```
