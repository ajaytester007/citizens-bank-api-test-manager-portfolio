from banking_api.core import BankingPaymentService

def test_payment_api_health_check():
    response = BankingPaymentService().health()
    assert response["status"] == "UP"
    assert response["service"] == "banking-payment-api"

def test_payment_api_rejects_missing_required_fields():
    response = BankingPaymentService().initiate_payment({"payment_id": "PMT-10001"})
    assert response["status_code"] == 400
    assert "Missing required fields" in response["error"]
