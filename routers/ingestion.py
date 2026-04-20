from fastapi import APIRouter
from models import IngestionSource
from typing import List
from data.mock_data import INGESTION_DATA

router = APIRouter()

@router.get("/status", response_model=List[IngestionSource])
def get_ingestion_status():
    return INGESTION_DATA

@router.get("/sources")
def get_sources():
    return {
        "sources": [
            {
                "name": "Municipal Corporation Portals",
                "type": "Government / PDF",
                "endpoints": ["dda.org.in", "mcgm.gov.in", "bmc.gov.in", "ghmc.gov.in"],
                "data_types": ["Infrastructure Tenders", "CLU Notifications", "Public Works Declarations"],
                "update_frequency": "Every 15 minutes"
            },
            {
                "name": "99acres",
                "type": "Commercial Portal",
                "endpoints": ["99acres.com"],
                "data_types": ["Listing Density", "Price per Sqft", "Search Volume"],
                "update_frequency": "Every 30 minutes"
            },
            {
                "name": "MagicBricks",
                "type": "Commercial Portal",
                "endpoints": ["magicbricks.com"],
                "data_types": ["Rental Listings", "Price Trends", "Demand Index"],
                "update_frequency": "Every 30 minutes"
            },
            {
                "name": "DDA / RERA Gazette",
                "type": "Regulatory",
                "endpoints": ["rera.delhi.gov.in", "maharera.mahaonline.gov.in"],
                "data_types": ["Project Approvals", "Zoning Changes", "Compliance Status"],
                "update_frequency": "Every 2 hours"
            },
            {
                "name": "Rental Yield Aggregator",
                "type": "Derived / Computed",
                "endpoints": ["internal pipeline"],
                "data_types": ["Rental Absorption Rate", "Yield Gap Index", "Occupancy Trends"],
                "update_frequency": "Every 3 hours"
            }
        ]
    }

@router.post("/trigger-refresh")
def trigger_refresh(source: str = "all"):
    return {
        "status": "refresh_queued",
        "source": source,
        "estimated_completion_seconds": 45,
        "job_id": "refresh_20260420_103045"
    }
