# ReadyAPI / SOAPUI Functional Verification Playbook

## ReadyAPI Validation Layers
1. Import WSDL/OpenAPI definition
2. Build functional test cases
3. Add status/header/payload assertions
4. Validate JSON/XML schema
5. Add property transfers for API chaining
6. Add Groovy scripts for dynamic test data
7. Use mock services for downstream systems
8. Export test evidence for release certification

## Mapped Repo Evidence
| ReadyAPI Concept | Repo Evidence |
|---|---|
| Service availability | `tests/l1_smoke` |
| Schema assertions | `tests/l2_contract` |
| API chaining | `tests/l3_workflow` |
| Downstream validation | `tests/l4_reconciliation` |
| Release evidence | `tests/l5_governance` |
