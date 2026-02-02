from pydantic import BaseModel, EmailStr
from typing import List, Optional
from enum import Enum

class IdentifierType(str, Enum):
    EMAIL = "email"
    USERNAME = "username"

class ScanRequest(BaseModel):
    identifier: str
    identifier_type: IdentifierType

class ExposureCategory(BaseModel):
    name: str
    platforms: List[str]
    risk_level: str  # low, medium, high
    explanation: str

class BreachInfo(BaseModel):
    name: str
    breach_date: Optional[str]
    data_exposed: List[str]
    action_required: str

class CleanupAction(BaseModel):
    priority: int
    action: str
    platforms: List[str]
    estimated_time: str

class ScanResponse(BaseModel):
    exposure_score: float
    risk_level: str
    categories: List[ExposureCategory]
    breaches: List[BreachInfo]
    cleanup_plan: List[CleanupAction]
    scan_timestamp: str
