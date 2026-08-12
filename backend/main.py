"""
KelanaAI - Main Presentation Layer
Sesi 2: Interactive Console Interface & Recommendation Engine
"""

import sys
import os

# Memastikan direktori utama bisa mengimpor folder services
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Impor logika bisnis dari services/trip_service.py
from services.trip_service import (
    get_trip_category,
    get_travel_session,
    calculate_daily_budget,
    get_recommended_places
)

def get_integer_input(prompt_text: str) -> int:
    """Helper validasi input integer (Jumlah Hari)."""
    while True:
        try:
            val = int(input(prompt_text))
            if val <= 0:
                print("⚠️  Jumlah hari harus lebih dari 0. Silakan coba lagi.")
                continue
            return val
        except ValueError:
            print("⚠️  Input tidak valid. Harap masukkan angka bulat!")

def get_float_input(prompt_text: str) -> float:
    """Helper validasi input float (Total Budget)."""
    while True:
        try:
            val = float(input(prompt_text))
            if val < 0:
                print("⚠️  Budget tidak boleh negatif. Silakan coba lagi.")
                continue
            return val
        except ValueError:
            print("⚠️  Input tidak valid. Harap masukkan angka desimal/bulat!")

def main():
    # 1. Menangani Interaksi Input Pengguna
    destination = input("Destination : ")
    days = get_integer_input("Days        : ")
    budget = get_float_input("Budget      : ")
    currency = input("Currency    : ")
    travel_month = input("Travel Month: ")

    # 2. Memanggil Fungsi Logika Bisnis dari Service Layer
    category = get_trip_category(budget)
    season = get_travel_session(travel_month)
    daily_budget = calculate_daily_budget(budget, days)
    recommended_places = get_recommended_places(destination)

    # Format angka agar tidak menampilkan desimal jika nilainya bulat (misal 1500)
    formatted_budget = int(budget) if budget.is_integer() else f"{budget:,.2f}"
    formatted_daily = int(daily_budget) if daily_budget.is_integer() else f"{daily_budget:,.2f}"

    # 3. Menampilkan Output Hasil Akhir (Sesuai Contoh Tampilan Soal)
    print("\n==================================")
    print("KelanaAI")
    print("==================================")
    print(f"Destination : {destination.strip().title()}")
    print(f"Days        : {days}")
    print(f"Budget      : {formatted_budget} {currency.strip().upper()}")
    print(f"Category    : {category}")
    print(f"Daily Budget: {formatted_daily} {currency.strip().upper()}/Day")
    print(f"Travel Month: {travel_month.strip().capitalize()}")
    print(f"Season      : {season}")
    print("\nRecommended Places")
    for place in recommended_places:
        print(f"- {place}")
    print("==================================")

if __name__ == "__main__":
    main()