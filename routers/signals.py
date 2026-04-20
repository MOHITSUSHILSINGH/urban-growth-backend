from fastapi import APIRouter, Query
from typing import List, Optional
from models import SignalResponse
from data.mock_data import SIGNALS_DATA

router = APIRouter()

@router.get("/", response_model=List[SignalResponse])
def get_signals(
    signal_type: Optional[str] = Query(None),
    zone: Optional[str] = Query(None),
    limit: int = Query(20, le=100)
):
    signals = SIGNALS_DATA
    if signal_type:
        signals = [s for s in signals if s["signal_type"].lower() == signal_type.lower()]
    if zone:
        signals = [s for s in signals if zone.lower() in s["zone"].lower()]
    return signals[:limit]

@router.get("/summary")
def get_signal_summary():
    from data.mock_data import SIGNALS_DATA
    by_type = {}
    for s in SIGNALS_DATA:
        t = s["signal_type"]
        by_type[t] = by_type.get(t, 0) + 1
    return {
        "total": len(SIGNALS_DATA),
        "by_type": by_type,
        "last_updated": "2026-04-20T10:30:00Z"
    }
