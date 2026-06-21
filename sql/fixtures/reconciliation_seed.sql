DROP TABLE IF EXISTS source_payments;
DROP TABLE IF EXISTS settlement_payments;
DROP TABLE IF EXISTS payment_reporting;

CREATE TABLE source_payments (payment_id TEXT PRIMARY KEY, customer_id TEXT, payment_amount NUMERIC, payment_status TEXT);
CREATE TABLE settlement_payments (payment_id TEXT PRIMARY KEY, settlement_amount NUMERIC, settlement_status TEXT);
CREATE TABLE payment_reporting (payment_id TEXT PRIMARY KEY, reported_amount NUMERIC, report_status TEXT);

INSERT INTO source_payments VALUES ('PMT-10001', 'CUST-5001', 1250.75, 'SETTLED');
INSERT INTO settlement_payments VALUES ('PMT-10001', 1250.75, 'SETTLED');
INSERT INTO payment_reporting VALUES ('PMT-10001', 1250.75, 'SETTLED');

INSERT INTO source_payments VALUES ('PMT-10002', 'CUST-5002', 990.00, 'SETTLED');
INSERT INTO settlement_payments VALUES ('PMT-10002', 980.00, 'SETTLED');
INSERT INTO payment_reporting VALUES ('PMT-10002', 990.00, 'SETTLED');
