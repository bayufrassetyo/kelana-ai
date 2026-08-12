"""
backend/services/trip_service.py
Layer: Business Logic Layer
"""

def get_trip_category(budget: float) -> str:
    if budget < 1000:
        return "Backpacker"
    elif 1000 <= budget <= 3000:
        return "Standard"
    else:
        return "Luxury"

def get_travel_session(month: str) -> str:
    formatted_month = month.strip().capitalize()
    if formatted_month == "December":
        return "Peak Season"
    elif formatted_month == "June":
        return "Holiday Season"
    else:
        return "Regular Season"

def calculate_daily_budget(budget: float, days: int) -> float:
    if days <= 0:
        return 0.0
    return budget / days

def get_recommended_places(destination: str) -> list:
    dest = destination.strip().lower()
    if "japan" in dest or "jepang" in dest:
        return ["Tokyo Tower", "Shibuya", "Mount Fuji"]
    elif "indonesia" in dest or "bali" in dest:
        return ["Kuta Beach", "Ubud Monkey Forest", "Tanah Lot"]
    elif "singapore" in dest or "singapura" in dest:
        return ["Marina Bay Sands", "Gardens by the Bay", "Sentosa Island"]
    else:
        return [f"City Center of {destination.title()}", f"Historical Museum of {destination.title()}", f"Local Market of {destination.title()}"]