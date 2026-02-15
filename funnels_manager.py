from typing import Dict, List, Optional
import logging
from datetime import datetime

class FunnelsManager:
    def __init__(self):
        self.funnels = {}  # type: Dict[str, Dict]
        self.logger = logging.getLogger(__name__)
        
    def create_funnel(self, funnel_id: str, config: Dict) -> Optional[str]:
        try:
            if not self._is_valid_config(config):
                raise ValueError("Invalid funnel configuration")
                
            new_funnel = {
                "id": funnel_id,
                "config": config,
                "created_at": datetime.now().isoformat(),
                "status": "active"
            }
            
            self.funnels[funnel_id] = new_funnel
            return funnel_id
            
        except Exception as e:
            self.logger.error(f"Failed to create funnel: {str(e)}")
            return None
    
    def _is_valid_config(self, config: Dict) -> bool:
        required_fields = ["name", "type", "affiliates"]
        return all(field in config for field in required_fields)