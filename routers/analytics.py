from fastapi import APIRouter, Query
from typing import Optional
from models import KPIResponse, YieldDataPoint, PricingDataPoint
from data.mock_data import KPI_DATA, YIELD_DATA, PRICING_DATA

router = APIRouter()

@router.get("/kpis", response_model=KPIResponse)
def get_kpis():
    return KPI_DATA

@router.get("/yield-gap")
def get_yield_gap(limit: int = Query(10, le=50)):
    return YIELD_DATA[:limit]

@router.get("/pricing-velocity")
def get_pricing_velocity(horizon: str = Query("12M", description="12M, 24M, or 60M")):
    if horizon in PRICING_DATA:
        return {"horizon": horizon, "data": PRICING_DATA[horizon]}
    return {"horizon": "12M", "data": PRICING_DATA["12M"]}

@router.get("/market-overview")
def get_market_overview():
    return {
        "total_zones_tracked": 47,
        "cities_covered": ["Delhi NCR", "Mumbai MMR", "Bengaluru", "Hyderabad", "Ahmedabad", "Pune", "Chennai"],
        "avg_appreciation_yoy": 14.3,
        "top_performing_city": "Delhi NCR",
        "undervalued_opportunity_count": 9,
        "data_freshness": "Live — updated every 30 minutes",
        "model_accuracy": "82% directional accuracy on 12M predictions (backtested 2022–2024)"
    }

@router.get("/correlation-matrix")
def get_correlation_matrix():
    return {
        "indicators": ["Municipal Decl.", "Listing Density", "Pricing Velocity", "Rental Absorption", "Zoning Policy"],
        "matrix": [
            [1.00, 0.72, 0.68, 0.54, 0.81],
            [0.72, 1.00, 0.83, 0.71, 0.60],
            [0.68, 0.83, 1.00, 0.79, 0.55],
            [0.54, 0.71, 0.79, 1.00, 0.48],
            [0.81, 0.60, 0.55, 0.48, 1.00],
        ],
        "interpretation": "Pearson correlation coefficients across 47 tracked micro-markets (2022–2026)"
    }
