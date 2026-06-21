# ReadyAPI / SOAPUI Suite Design

## Suite: Banking Payment API Regression

### Test Case 1: Payment Initiation
Validate request schema, authentication header, HTTP 201 response, and status INITIATED.

### Test Case 2: Payment Posting
Transfer payment_id from initiation response and validate INITIATED → POSTED.

### Test Case 3: Settlement
Validate POSTED → SETTLED and downstream settlement record.

### Test Case 4: Negative Workflow
Attempt settlement before posting and validate conflict response.

### Test Case 5: ISO 20022 XML Message
Validate XML against XSD and required payment fields.

### Service Virtualization
Mock settlement processor, fraud screening response, and downstream reporting acknowledgment.
