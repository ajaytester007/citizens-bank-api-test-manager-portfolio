SELECT
    src.payment_id,
    src.customer_id,
    src.payment_amount AS source_amount,
    stl.settlement_amount,
    rpt.reported_amount,
    src.payment_status,
    stl.settlement_status,
    rpt.report_status,
    CASE
        WHEN src.payment_amount = stl.settlement_amount
         AND stl.settlement_amount = rpt.reported_amount
         AND src.payment_status = stl.settlement_status
         AND stl.settlement_status = rpt.report_status
        THEN 'PASS'
        ELSE 'FAIL'
    END AS reconciliation_status
FROM source_payments src
LEFT JOIN settlement_payments stl ON src.payment_id = stl.payment_id
LEFT JOIN payment_reporting rpt ON src.payment_id = rpt.payment_id
ORDER BY src.payment_id;
