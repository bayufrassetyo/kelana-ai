"""
KelanaAI - Web Presentation Layer (FastAPI)
Sesi 3: REST API Implementation + Homework Endpoints
"""

import sys
import os
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Memastikan direktori utama bisa mengimpor folder services
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import fungsi logika bisnis dari trip_service.py (TANPA MENGUBAH TRIP_SERVICE.PY)
from services.trip_service import (
    calculate_daily_budget,
    get_trip_category
)

# Inisialisasi Aplikasi FastAPI
app = FastAPI(
    title="KelanaAI API",
    description="REST API untuk Perencana Perjalanan KelanaAI",
    version="1.0.0"
)

# 1. Pydantic Model untuk Request Body
class TripRequest(BaseModel):
    destination: str = Field(..., example="Japan")
    days: int = Field(..., gt=0, example=5)
    budget: float = Field(..., ge=0, example=2000)


# 2. Endpoint 1 — GET /
@app.get("/")
def read_root():
    return {"message": "Welcome to KelanaAI"}


# 3. Endpoint 2 — GET /health
@app.get("/health")
def health_check():
    return {"status": "OK"}


# 4. Endpoint 3 — POST /api/v1/trips
@app.post("/api/v1/trips")
def create_trip_plan(request: TripRequest):
    daily_budget = calculate_daily_budget(request.budget, request.days)
    category = get_trip_category(request.budget)
    
    return {
        "destination": request.destination,
        "days": request.days,
        "budget": request.budget,
        "daily_budget": daily_budget,
        "category": category
    }


# ==========================================
# HOMEWORK ENDPOINTS (Sesi 3 Extension)
# ==========================================

# 5. Endpoint 4 — GET /api/v1/recommendations
@app.get("/api/v1/recommendations")
def get_recommendations():
    return ["Tokyo Tower", "Mount Fuji", "Shibuya"]


# 6. Endpoint 5 — GET /api/v1/transportations
@app.get("/api/v1/transportations")
def get_transportations():
    return ["Bus", "Train", "Flight"]