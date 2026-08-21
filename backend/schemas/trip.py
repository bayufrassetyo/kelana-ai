from pydantic import BaseModel

class TripCreate(BaseModel):
    destination: str
    days: int
    budget: float

class TripUpdate(BaseModel):
    budget: float

class TripResponse(BaseModel):
    id: int
    destination: str
    days: int
    budget: float
    category: str
    daily_budget: float

    class Config:
        from_attributes = True