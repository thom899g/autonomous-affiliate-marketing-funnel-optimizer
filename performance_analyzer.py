import logging
from typing import Dict, List
import pandas as pd

class PerformanceAnalyzer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def analyze_performance(self, funnel_id: str, metrics: Dict) -> Optional[Dict]:
        try:
            df = pd.DataFrame(metrics)
            analysis = {
                "conversion_rate": self._calculate_conversion_rate(df),
                "ctr": self._calculate_ctr(df),
                "revenue_per_click": self._calculate_revenue_per_click(df)
            }
            
            return analysis
            
        except Exception as e:
            self.logger.error(f"Performance analysis failed: {str(e)}")
            return None
    
    def _calculate_conversion_rate(self, df: pd.DataFrame) -> float:
        converted = df[df['action'] == 'conversion'].shape[0]
        total_visitors = df.shape[0]
        return converted / total_visitors if total_visitors > 0 else 0

    def _calculate_ctr(self, df: pd.DataFrame) -> float:
        clicked = df[df['action'] == 'click'].shape[0]
        impressions = df[df['action'] == 'impression'].shape[0]
        return clicked / impressions if impressions > 0 else 0

    def _calculate_revenue_per_click(self, df: pd.DataFrame) -> float:
        total_rev = df[df['action'] == 'conversion']['revenue'].sum()
        clicked = df[df['action'] == 'click'].shape[0]
        return total_rev / clicked if clicked > 0 else 0