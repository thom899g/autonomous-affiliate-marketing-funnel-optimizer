import logging
from typing import Dict, List

class ComplianceMonitor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def monitor_compliance(self, funnel_id: str, data: Dict) -> bool:
        try:
            # Check for prohibited content
            if any(keyword in data.get("content", "") for keyword in ["illegal", "fraud"]):
                self._log_non_compliance(funnel_id)
                return False
                
            # Check for policy adherence
            if not self._check_affiliate_policy(data):
                self._log_non_compliance(funnel_id)
                return False
                
            return True
            
        except Exception as e:
            self.logger.error(f"Compliance check failed: {str(e)}")
            return False
    
    def _check_affiliate_policy(self, data: Dict) -> bool:
        # Simplified policy check
        if data.get("platform") == "amazon":
            return self._check_amazon_policies(data)
        elif data.get("platform") in ["clickbank", "shareasale"]:
            return self._check_general_policies(data)
        return False
    
    def _check_amazon_policies(self, data: Dict) -> bool:
        # Example Amazon policy checks
        if data.get("product_category") == "electronics":
            return True
        return False
    
    def _log_non_compliance(self, funnel_id: str) -> None:
        self.logger.info(f"Non-compliance detected for funnel {funnel_id}")