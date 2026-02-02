from typing import List
from app.api.models import ExposureCategory, BreachInfo, CleanupAction

class RiskScorer:
    """Risk calculation and cleanup plan generation"""
    
    RISK_WEIGHTS = {
        "low": 2,
        "medium": 5,
        "high": 10
    }
    
    def calculate_score(self, categories: List[ExposureCategory], breaches: List[BreachInfo]) -> float:
        """Calculate 0-100 risk score"""
        category_score = sum(self.RISK_WEIGHTS.get(cat.risk_level, 0) for cat in categories)
        breach_score = len(breaches) * 15  # Each breach adds 15 points
        
        total = category_score + breach_score
        return min(total, 100.0)  # Cap at 100
    
    def get_risk_level(self, score: float) -> str:
        """Convert score to risk level"""
        if score < 30:
            return "low"
        elif score < 60:
            return "medium"
        else:
            return "high"
    
    def generate_cleanup_plan(self, categories: List[ExposureCategory]) -> List[CleanupAction]:
        """Generate prioritized cleanup steps"""
        return [
            CleanupAction(
                priority=1,
                action="Delete unused accounts",
                platforms=["Old social media", "Inactive forums"],
                estimated_time="15 minutes"
            ),
            CleanupAction(
                priority=2,
                action="Update passwords",
                platforms=["Email", "Banking", "Primary social media"],
                estimated_time="30 minutes"
            ),
            CleanupAction(
                priority=3,
                action="Review privacy settings",
                platforms=[cat.platforms[0] for cat in categories if cat.platforms],
                estimated_time="20 minutes"
            )
        ]
