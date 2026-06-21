from dataclasses import dataclass, asdict
from decimal import Decimal
from typing import Dict, Any

@dataclass
class Payment:
    payment_id: str
    customer_id: str
    payment_type: str
    amount: Decimal
    currency: str
    status: str = "INITIATED"

class BankingPaymentService:
    """In-memory banking payment workflow simulator for portfolio validation."""
    def __init__(self):
        self.payments: Dict[str, Payment] = {}
        self.settlements: Dict[str, Dict[str, Any]] = {}

    def health(self):
        return {"status": "UP", "service": "banking-payment-api"}

    def initiate_payment(self, payload):
        required = ["payment_id", "customer_id", "payment_type", "amount", "currency"]
        missing = [field for field in required if field not in payload]
        if missing:
            return {"status_code": 400, "error": f"Missing required fields: {missing}"}
        if Decimal(str(payload["amount"])) <= 0:
            return {"status_code": 422, "error": "Payment amount must be greater than zero"}
        payment = Payment(payload["payment_id"], payload["customer_id"], payload["payment_type"],
                          Decimal(str(payload["amount"])), payload["currency"])
        self.payments[payment.payment_id] = payment
        return {"status_code": 201, "payment": self._serialize(payment)}

    def post_payment(self, payment_id):
        payment = self.payments.get(payment_id)
        if not payment:
            return {"status_code": 404, "error": "Payment not found"}
        payment.status = "POSTED"
        return {"status_code": 200, "payment": self._serialize(payment)}

    def settle_payment(self, payment_id):
        payment = self.payments.get(payment_id)
        if not payment:
            return {"status_code": 404, "error": "Payment not found"}
        if payment.status != "POSTED":
            return {"status_code": 409, "error": "Payment must be POSTED before settlement"}
        payment.status = "SETTLED"
        self.settlements[payment_id] = {
            "payment_id": payment_id,
            "settlement_amount": str(payment.amount),
            "settlement_status": "SETTLED",
            "currency": payment.currency
        }
        return {"status_code": 200, "payment": self._serialize(payment)}

    def get_payment_status(self, payment_id):
        payment = self.payments.get(payment_id)
        if not payment:
            return {"status_code": 404, "error": "Payment not found"}
        return {"status_code": 200, "payment": self._serialize(payment)}

    @staticmethod
    def _serialize(payment):
        data = asdict(payment)
        data["amount"] = str(payment.amount)
        return data
