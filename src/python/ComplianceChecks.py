from datetime import datetime
import yaml

class ComplianceValidator:
    def __init__(self):
        self.rules = self._load_compliance_rules()
        self.validation_timestamp = datetime.now()

    def _load_compliance_rules(self):
        """
        Load compliance rules from configuration
        """
        try:
            with open("config/compliance_rules.yaml", "r") as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            # Default rules if config not found
            return {
                "ECOSOC_RULE_1": {
                    "name": "Active Status Check",
                    "description": "Fund must have active compliance status",
                    "severity": "HIGH"
                }
            }

    def get_compliance_rules(self):
        """
        Get all compliance rules
        """
        return self.rules

    def validate_compliance(self, data):
        """
        Validate data against compliance rules
        """
        violations = []
        
        # Check active status
        if data.get("compliance_status") != "ACTIVE":
            violations.append({
                "rule": "ECOSOC_RULE_1",
                "description": "Fund is not in active compliance status"
            })

        # Check last review date
        try:
            last_review = datetime.strptime(data.get("last_review_date"), "%Y-%m-%d")
            if (datetime.now() - last_review).days > 365:
                violations.append({
                    "rule": "ECOSOC_RULE_2",
                    "description": "Annual review overdue"
                })
        except (ValueError, TypeError):
            violations.append({
                "rule": "ECOSOC_RULE_2",
                "description": "Invalid last review date"
            })

        return {
            "is_compliant": len(violations) == 0,
            "violations": violations,
            "fund_id": data.get("fund_id"),
            "timestamp": datetime.now().isoformat()
        }

    def generate_compliance_report(self):
        """
        Generate compliance status report
        """
        return {
            "timestamp": self.validation_timestamp.isoformat(),
            "compliance_score": 0.95,  # Placeholder score
            "violations": [],  # Placeholder for actual violations
            "rules_checked": len(self.rules),
            "status": "COMPLIANT"
        } 