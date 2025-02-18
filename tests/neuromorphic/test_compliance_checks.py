import pytest
from python.ComplianceChecks import ComplianceValidator

def test_compliance_validator_initialization():
    validator = ComplianceValidator()
    assert validator is not None

def test_ecosoc_compliance_rules():
    validator = ComplianceValidator()
    rules = validator.get_compliance_rules()
    assert len(rules) > 0
    assert "ECOSOC_RULE_1" in rules

def test_compliance_validation():
    validator = ComplianceValidator()
    test_data = {
        "fund_id": "TEST001",
        "compliance_status": "ACTIVE",
        "last_review_date": "2024-01-01"
    }
    result = validator.validate_compliance(test_data)
    assert result["is_compliant"] is True

def test_compliance_reporting():
    validator = ComplianceValidator()
    report = validator.generate_compliance_report()
    assert "timestamp" in report
    assert "compliance_score" in report
    assert "violations" in report 