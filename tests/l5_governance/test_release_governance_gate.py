def calculate_release_readiness_score(metrics):
    weights = {"api_pass_rate":0.30,"reconciliation_pass_rate":0.25,"critical_defect_score":0.25,"uat_signoff_score":0.10,"deployment_readiness_score":0.10}
    return sum(metrics[k] * w for k, w in weights.items())

def test_release_readiness_go_decision():
    metrics = {"api_pass_rate":100,"reconciliation_pass_rate":100,"critical_defect_score":100,"uat_signoff_score":100,"deployment_readiness_score":100}
    assert calculate_release_readiness_score(metrics) >= 95

def test_release_readiness_no_go_when_critical_defects_exist():
    metrics = {"api_pass_rate":98,"reconciliation_pass_rate":100,"critical_defect_score":0,"uat_signoff_score":100,"deployment_readiness_score":100}
    assert calculate_release_readiness_score(metrics) < 95
