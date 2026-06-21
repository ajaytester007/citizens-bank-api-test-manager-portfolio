import sqlite3
from pathlib import Path

def test_payment_reconciliation_identifies_pass_and_fail_controls():
    conn = sqlite3.connect(":memory:")
    conn.executescript(Path("sql/fixtures/reconciliation_seed.sql").read_text())
    rows = conn.execute(Path("sql/reconciliation/payment_reconciliation.sql").read_text()).fetchall()
    results = {row[0]: row[-1] for row in rows}
    assert results["PMT-10001"] == "PASS"
    assert results["PMT-10002"] == "FAIL"
