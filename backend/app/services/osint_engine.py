from typing import List, Dict
from app.api.models import ExposureCategory, IdentifierType
import re

class OSINTEngine:
    """OSINT scanning engine - rule-based pattern matching"""
    
    # Email domain patterns
    COMMON_DOMAINS = {
        "gmail.com", "yahoo.com", "outlook.com", "hotmail.com",
        "protonmail.com", "icloud.com", "aol.com"
    }
    
    CORPORATE_DOMAINS = {
        "company.com", "corp.com", "inc.com", "ltd.com"
    }
    
    EDU_DOMAINS = {
        ".edu", ".ac.in", "university", "college", "school"
    }
    
    # Platform categories with detection rules
    PLATFORM_CATEGORIES = {
        "social_media": {
            "name": "Social Media",
            "platforms": ["Facebook", "Instagram", "Twitter/X", "LinkedIn", "Snapchat"],
            "risk_weight": 5,
            "triggers": ["gmail", "yahoo", "outlook", "common_email"],
            "explanation": "Personal email addresses are commonly used for social media signups. Your profile data, posts, and photos may be publicly searchable or visible to connections."
        },
        "professional": {
            "name": "Professional Networks",
            "platforms": ["LinkedIn", "GitHub", "Stack Overflow", "Medium", "Dev.to"],
            "risk_weight": 4,
            "triggers": ["professional_email", "username", "corporate_domain"],
            "explanation": "Professional profiles typically contain your work history, skills, projects, and educational background. This data is intentionally public for networking."
        },
        "ecommerce_india": {
            "name": "E-Commerce (India)",
            "platforms": ["Amazon India", "Flipkart", "Myntra", "Meesho", "Ajio"],
            "risk_weight": 6,
            "triggers": ["gmail", "yahoo", "outlook", "any_email"],
            "explanation": "Shopping platforms store your delivery addresses, phone numbers, payment methods (last 4 digits), and purchase history."
        },
        "food_delivery": {
            "name": "Food & Delivery Apps",
            "platforms": ["Swiggy", "Zomato", "Dunzo", "Blinkit", "Zepto"],
            "risk_weight": 6,
            "triggers": ["gmail", "phone_likely"],
            "explanation": "Food delivery apps have your home/office addresses, phone number, and location history from past orders."
        },
        "job_portals": {
            "name": "Job Portals (India)",
            "platforms": ["Naukri", "LinkedIn", "Indeed", "Monster India", "Shine"],
            "risk_weight": 7,
            "triggers": ["professional_email", "gmail", "any_email"],
            "explanation": "Job portals store comprehensive data: full resume, phone number, current/past employers, salary expectations, and educational certificates."
        },
        "fintech": {
            "name": "Financial & Payment Apps",
            "platforms": ["Paytm", "PhonePe", "Google Pay", "CRED", "Razorpay"],
            "risk_weight": 9,
            "triggers": ["phone_likely", "gmail"],
            "explanation": "Payment apps are linked to your bank accounts, UPI ID, transaction history, and may have KYC documents (Aadhaar, PAN)."
        },
        "edtech": {
            "name": "Education & Learning",
            "platforms": ["Coursera", "Udemy", "NPTEL", "Unacademy", "BYJU'S"],
            "risk_weight": 3,
            "triggers": ["edu_email", "gmail", "student_pattern"],
            "explanation": "Ed-tech platforms have your learning history, certificates, and possibly payment information if you've made purchases."
        },
        "streaming": {
            "name": "Streaming & Entertainment",
            "platforms": ["Netflix", "Amazon Prime", "Hotstar", "Spotify", "YouTube"],
            "risk_weight": 4,
            "triggers": ["gmail", "any_email"],
            "explanation": "Streaming services store viewing habits, preferences, payment methods, and device information."
        },
        "travel": {
            "name": "Travel & Booking",
            "platforms": ["MakeMyTrip", "Goibibo", "OYO", "Airbnb", "Ola", "Uber"],
            "risk_weight": 7,
            "triggers": ["gmail", "phone_likely"],
            "explanation": "Travel apps store your ID proof (for bookings), travel history, payment details, and frequently visited locations."
        },
        "communication": {
            "name": "Communication Apps",
            "platforms": ["WhatsApp", "Telegram", "Discord", "Slack", "Microsoft Teams"],
            "risk_weight": 5,
            "triggers": ["phone_likely", "any_email", "username"],
            "explanation": "Communication apps have your phone number, profile photo, status updates, and group memberships."
        },
        "gaming": {
            "name": "Gaming Platforms",
            "platforms": ["Steam", "Epic Games", "PlayStation", "Xbox Live", "Mobile Gaming Apps"],
            "risk_weight": 4,
            "triggers": ["username", "gmail"],
            "explanation": "Gaming accounts contain username, gaming history, friends list, and payment information for in-game purchases."
        }
    }
    
    async def scan(self, identifier: str, id_type: IdentifierType) -> List[ExposureCategory]:
        """Main scanning logic"""
        results = []
        
        if id_type == IdentifierType.EMAIL:
            results.extend(await self._scan_email(identifier))
        elif id_type == IdentifierType.USERNAME:
            results.extend(await self._scan_username(identifier))
        
        return results
    
    async def _scan_email(self, email: str) -> List[ExposureCategory]:
        """Email pattern matching and platform detection"""
        categories = []
        email = email.lower().strip()
        
        # Extract domain
        if "@" not in email:
            return categories
        
        username_part, domain = email.split("@", 1)
        
        # Detect email type
        is_common_email = domain in self.COMMON_DOMAINS
        is_corporate = any(corp in domain for corp in self.CORPORATE_DOMAINS)
        is_edu = any(edu in domain for edu in self.EDU_DOMAINS)
        is_custom_domain = not (is_common_email or is_corporate or is_edu)
        
        # Match platforms based on email patterns
        for category_key, category_data in self.PLATFORM_CATEGORIES.items():
            triggers = category_data["triggers"]
            should_include = False
            
            # Check trigger conditions
            if "any_email" in triggers:
                should_include = True
            elif "gmail" in triggers and domain == "gmail.com":
                should_include = True
            elif "yahoo" in triggers and domain == "yahoo.com":
                should_include = True
            elif "outlook" in triggers and domain in ["outlook.com", "hotmail.com"]:
                should_include = True
            elif "common_email" in triggers and is_common_email:
                should_include = True
            elif "professional_email" in triggers and (is_corporate or is_edu):
                should_include = True
            elif "corporate_domain" in triggers and is_corporate:
                should_include = True
            elif "edu_email" in triggers and is_edu:
                should_include = True
            elif "phone_likely" in triggers:
                # Phone-first apps, but emails also used
                should_include = True
            
            if should_include:
                # Determine risk level based on weight
                risk_level = self._get_risk_level(category_data["risk_weight"])
                
                categories.append(ExposureCategory(
                    name=category_data["name"],
                    platforms=category_data["platforms"],
                    risk_level=risk_level,
                    explanation=category_data["explanation"]
                ))
        
        return categories
    
    async def _scan_username(self, username: str) -> List[ExposureCategory]:
        """Username enumeration and platform detection"""
        categories = []
        username = username.lower().strip()
        
        # Common platforms that use usernames
        username_platforms = [
            ("social_media", "Social Media", 
             ["Twitter/X", "Instagram", "TikTok", "Reddit", "Pinterest"],
             "medium",
             "Your username may be registered on social platforms. Public posts, comments, and follower/following lists may be visible."),
            
            ("developer_platforms", "Developer Platforms",
             ["GitHub", "GitLab", "Stack Overflow", "HackerRank", "LeetCode"],
             "low",
             "Developer profiles show your code repositories, contributions, problem-solving activity, and technical discussions."),
            
            ("gaming", "Gaming Platforms",
             ["Steam", "Discord", "Twitch", "Epic Games", "Roblox"],
             "low",
             "Gaming usernames reveal your gaming activity, friends list, achievements, and playtime statistics."),
            
            ("forums", "Forums & Communities",
             ["Reddit", "Quora", "Medium", "Dev.to", "Hacker News"],
             "medium",
             "Forum accounts contain your post history, comments, interests, and interaction patterns with communities.")
        ]
        
        for platform_id, name, platforms, risk, explanation in username_platforms:
            categories.append(ExposureCategory(
                name=name,
                platforms=platforms,
                risk_level=risk,
                explanation=explanation
            ))
        
        return categories
    
    def _get_risk_level(self, weight: int) -> str:
        """Convert weight to risk level"""
        if weight >= 8:
            return "high"
        elif weight >= 5:
            return "medium"
        else:
            return "low"
    
    def _detect_username_pattern(self, username: str) -> Dict[str, bool]:
        """Analyze username for patterns"""
        return {
            "has_numbers": bool(re.search(r'\d', username)),
            "has_special_chars": bool(re.search(r'[^a-zA-Z0-9_]', username)),
            "is_common_format": bool(re.match(r'^[a-z]+[0-9]{2,4}$', username)),
            "length": len(username)
        }
