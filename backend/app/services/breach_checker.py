import httpx
from typing import List
from app.api.models import BreachInfo

class BreachChecker:
    """Have I Been Pwned API integration"""
    
    HIBP_API = "https://haveibeenpwned.com/api/v3/breachedaccount"
    
    async def check(self, identifier: str) -> List[BreachInfo]:
        """Check for known breaches"""
        breaches = []
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.HIBP_API}/{identifier}",
                    headers={"User-Agent": "DataFootprintMapper"},
                    timeout=10.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    for breach in data[:5]:  # Limit to 5 most relevant
                        breaches.append(BreachInfo(
                            name=breach.get("Name", "Unknown"),
                            breach_date=breach.get("BreachDate"),
                            data_exposed=breach.get("DataClasses", []),
                            action_required=self._get_action(breach.get("DataClasses", []))
                        ))
        
        except Exception:
            # Fail gracefully if API is down
            pass
        
        return breaches
    
    def _get_action(self, data_classes: List[str]) -> str:
        """Generate actionable advice"""
        if "Passwords" in data_classes:
            return "Change your password immediately on affected platforms"
        elif "Email addresses" in data_classes:
            return "Monitor for phishing emails and spam"
        else:
            return "Stay alert for targeted scams using your exposed data"
