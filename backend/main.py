import sys
import os
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Memastikan direktori backend/ dan root masuk ke sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import langsung dari modul lokal (TANPA awalan 'backend.')
from database import SessionLocal, init_db
from models.trip import Trip
from schemas.trip import TripCreate, TripUpdate, TripResponse
from services.trip_service import calculate_daily_budget, get_trip_category

# Inisialisasi tabel di PostgreSQL saat aplikasi berjalan
init_db()

app = FastAPI(
    title="KelanaAI API",
    description="REST API untuk Perencana Perjalanan KelanaAI (Sesi 4 - Database Persistence)",
    version="2.0.0"
)

# Dependency DB Session Lifecycle
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. Endpoint Home & Health Check
@app.get("/")
def read_root():
    return {"message": "Welcome to KelanaAI API"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

# 2. [POST] Create Trip (Simpan ke Database PostgreSQL)
@app.post("/api/v1/trips", response_model=TripResponse, status_code=status.HTTP_201_CREATED)
def create_trip(request: TripCreate, db: Session = Depends(get_db)):
    daily_budget = calculate_daily_budget(request.budget, request.days)
    category = get_trip_category(request.budget)
    
    trip = Trip(
        destination=request.destination,
        days=request.days,
        budget=request.budget,
        category=category,
        daily_budget=daily_budget
    )
    db.add(trip)
    db.commit()
    db.refresh(trip)
    return trip

# 3. [GET] List All Trips
@app.get("/api/v1/trips", response_model=List[TripResponse])
def list_trips(db: Session = Depends(get_db)):
    return db.query(Trip).all()

# 4. [GET] Get Trip by ID
@app.get("/api/v1/trips/{trip_id}", response_model=TripResponse)
def get_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Trip with id {trip_id} not found"
        )
    return trip

# ==========================================
# HOMEWORK SESI 4: PUT & DELETE ENDPOINTS
# ==========================================

# 5. [PUT] Update Budget & Recalculate
@app.put("/api/v1/trips/{trip_id}", response_model=TripResponse)
def update_trip_budget(trip_id: int, request: TripUpdate, db: Session = Depends(get_db)):
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Trip with id {trip_id} not found"
        )
    
    trip.budget = request.budget
    trip.daily_budget = calculate_daily_budget(request.budget, trip.days)
    trip.category = get_trip_category(request.budget)
    
    db.commit()
    db.refresh(trip)
    return trip

# 6. [DELETE] Delete Trip by ID
@app.delete("/api/v1/trips/{trip_id}", status_code=status.HTTP_200_OK)
def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Trip with id {trip_id} not found"
        )
    
    db.delete(trip)
    db.commit()
    return {"message": f"Trip with id {trip_id} successfully deleted"}