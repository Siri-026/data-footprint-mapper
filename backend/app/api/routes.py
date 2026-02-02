from fastapi import APIRouter, HTTPException, Request
from app.api.models import ScanRequest, ScanResponse, ExposureCategory, CleanupAction
from app.services.osint_engine import OSINTEngine
from datetime import datetime

router = APIRouter()

@router.post("/scan", response_model=ScanResponse)
async def scan_footprint(request: Request, scan_req: ScanRequest):
    try:
        # OSINT scanning
        osint = OSINTEngine()
        exposure_data = await osint.scan(scan_req.identifier, scan_req.identifier_type)
        
        # Simple risk scoring
        score = len(exposure_data) * 8.5  # Each category adds ~8.5 points
        score = min(score, 100.0)  # Cap at 100
        
        # Determine risk level
        if score < 30:
            risk_level = "low"
        elif score < 60:
            risk_level = "medium"
        else:
            risk_level = "high"
        
        # Generate cleanup plan
        cleanup = [
            CleanupAction(
                priority=1,
                action="Review and delete unused accounts",
                platforms=["Old social media", "Inactive shopping accounts"],
                estimated_time="15-20 minutes"
            ),
            CleanupAction(
                priority=2,
                action="Update privacy settings on active accounts",
                platforms=[cat.platforms[0] for cat in exposure_data[:3] if cat.platforms],
                estimated_time="20-30 minutes"
            ),
            CleanupAction(
                priority=3,
                action="Enable two-factor authentication",
                platforms=["Email", "Banking apps", "Payment apps"],
                estimated_time="10-15 minutes"
            )
        ]
        
        return ScanResponse(
            exposure_score=round(score, 1),
            risk_level=risk_level,
            categories=exposure_data,
            breaches=[],  # Will implement HIBP later
            cleanup_plan=cleanup,
            scan_timestamp=datetime.utcnow().isoformat()
        )
    
    except Exception as e:
        print(f"Error in scan: {str(e)}")  # Debug log
        raise HTTPException(status_code=500, detail=f"Scan failed: {str(e)}")

@router.get("/health")
async def health_check():
    return {"status": "healthy"}
