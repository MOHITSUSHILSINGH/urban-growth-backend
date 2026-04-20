from fastapi import APIRouter
from models import HeatmapResponse
from data.mock_data import HEATMAP_DATA

router = APIRouter()

@router.get("/", response_model=HeatmapResponse)
def get_heatmap():
    return HEATMAP_DATA

@router.get("/gvs-algorithm")
def get_gvs_algorithm_info():
    return {
        "description": "Growth Velocity Score (GVS) Calculation Algorithm",
        "version": "2.1",
        "weights": {
            "municipal_declarations": 0.35,
            "listing_density_trend": 0.20,
            "pricing_velocity": 0.20,
            "rental_absorption": 0.15,
            "zoning_policy_signals": 0.10
        },
        "formula": "GVS = Σ(weight_i × normalized_score_i) × 100",
        "normalization": "Min-max normalization per indicator across all zones",
        "horizon_decay": "GVS scores decay by 0.92^n per 12M horizon for uncertainty adjustment"
    }
