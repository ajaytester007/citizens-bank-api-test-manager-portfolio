from banking_api.core import BankingPaymentService

def test_payment_initiation_posting_settlement_lifecycle():
    service = BankingPaymentService()
    payload = {"payment_id":"PMT-20001","customer_id":"CUST-6001","payment_type":"WIRE","amount":5000.00,"currency":"USD"}
    assert service.initiate_payment(payload)["payment"]["status"] == "INITIATED"
    assert service.post_payment("PMT-20001")["payment"]["status"] == "POSTED"
    assert service.settle_payment("PMT-20001")["payment"]["status"] == "SETTLED"
    assert service.get_payment_status("PMT-20001")["payment"]["status"] == "SETTLED"

def test_payment_cannot_settle_before_posting():
    service = BankingPaymentService()
    payload = {"payment_id":"PMT-20002","customer_id":"CUST-6002","payment_type":"RTP","amount":100.00,"currency":"USD"}
    service.initiate_payment(payload)
    settlement = service.settle_payment("PMT-20002")
    assert settlement["status_code"] == 409
