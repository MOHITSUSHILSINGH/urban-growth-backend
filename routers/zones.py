from fastapi import APIRouter, Query
from typing import List, Optional
from models import ZoneResponse
from data.mock_data import ZONES_DATA

router = APIRouter()

@router.get("/", response_model=List[ZoneResponse])
def get_zones(
    min_gvs: Optional[float] = Query(None, description="Minimum GVS score"),
    state: Optional[str] = Query(None, description="Filter by state"),
    undervalued: Optional[bool] = Query(None, description="Filter undervalued zones"),
    limit: int = Query(20, le=100)
):
    zones = ZONES_DATA
    if min_gvs is not None:
        zones = [z for z in zones if z["gvs"] >= min_gvs]
    if state:
        zones = [z for z in zones if z["state"].lower() == state.lower()]
    if undervalued is not None:
        zones = [z for z in zones if z["undervalued"] == undervalued]
    zones = sorted(zones, key=lambda x: x["gvs"], reverse=True)
    return zones[:limit]

@router.get("/{zone_id}", response_model=ZoneResponse)
def get_zone(zone_id: str):
    for z in ZONES_DATA:
        if z["id"] == zone_id:
            return z
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Zone not found")

@router.get("/{zone_id}/analysis")
def get_zone_analysis(zone_id: str):
    for z in ZONES_DATA:
        if z["id"] == zone_id:
            return {
                "zone": z,
                "infrastructure_catalysts": [
                    {"type": "Metro Expansion", "status": "Tendered", "completion": "2027Q2", "impact_score": 88},
                    {"type": "Airport Connectivity", "status": "Under Construction", "completion": "2026Q4", "impact_score": 75},
                    {"type": "Highway Upgrade", "status": "Approved", "completion": "2028Q1", "impact_score": 62},
                ],
                "risk_factors": [
                    {"factor": "Regulatory Delay Risk", "level": "Medium", "mitigation": "CLU already in place"},
                    {"factor": "Market Saturation", "level": "Low", "mitigation": "Listing density still below threshold"},
                    {"factor": "Financing Rate Risk", "level": "Medium", "mitigation": "Diversify across RTM and UC"},
                ],
                "investment_recommendation": "Strong Buy — 24–36M horizon",
                "target_roi_range": "18–26%",
            }
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Zone not found")
