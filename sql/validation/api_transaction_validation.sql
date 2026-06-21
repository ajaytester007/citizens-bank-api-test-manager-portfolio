-- API Transaction Validation
-- Purpose: Validate API transaction records against backend processing and reporting tables.

SELECT
    api.correlation_id,
    api.api_name,
    api.request_timestamp,
    txn.transaction_id,
    txn.transaction_status,
    rpt.report_status,
    CASE
        WHEN txn.transaction_status = rpt.report_status THEN 'PASS'
        ELSE 'FAIL'
    END AS validation_status
FROM api_request_log api
JOIN transaction_master txn
    ON api.correlation_id = txn.correlation_id
LEFT JOIN transaction_report rpt
    ON txn.transaction_id = rpt.transaction_id;
