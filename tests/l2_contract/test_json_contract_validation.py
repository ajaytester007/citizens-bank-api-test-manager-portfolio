import json
from pathlib import Path
from jsonschema import validate, ValidationError

SCHEMA = json.loads(Path("schemas/json/payment-initiation-schema.json").read_text())

def test_valid_payment_request_matches_contract():
    payload = {"payment_id":"PMT-10001","customer_id":"CUST-5001","payment_type":"ACH","amount":1250.75,"currency":"USD"}
    validate(instance=payload, schema=SCHEMA)

def test_invalid_payment_type_fails_contract():
    payload = {"payment_id":"PMT-10001","customer_id":"CUST-5001","payment_type":"CRYPTO","amount":1250.75,"currency":"USD"}
    try:
        validate(instance=payload, schema=SCHEMA)
    except ValidationError:
        assert True
    else:
        raise AssertionError("Invalid payment_type should fail schema validation")
