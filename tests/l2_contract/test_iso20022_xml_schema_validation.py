from pathlib import Path
from lxml import etree

def test_iso20022_style_payment_xml_matches_xsd():
    schema = etree.XMLSchema(etree.parse(str(Path("schemas/xml/iso20022-payment.xsd"))))
    xml = etree.fromstring(b'''<CustomerCreditTransfer><MessageId>MSG-10001</MessageId><DebtorAccount>DA-111111</DebtorAccount><CreditorAccount>CA-222222</CreditorAccount><Amount>1250.75</Amount><Currency>USD</Currency><SettlementDate>2026-06-20</SettlementDate></CustomerCreditTransfer>''')
    assert schema.validate(xml)

def test_iso20022_style_payment_xml_rejects_missing_amount():
    schema = etree.XMLSchema(etree.parse(str(Path("schemas/xml/iso20022-payment.xsd"))))
    xml = etree.fromstring(b'''<CustomerCreditTransfer><MessageId>MSG-10001</MessageId><DebtorAccount>DA-111111</DebtorAccount><CreditorAccount>CA-222222</CreditorAccount><Currency>USD</Currency><SettlementDate>2026-06-20</SettlementDate></CustomerCreditTransfer>''')
    assert not schema.validate(xml)
