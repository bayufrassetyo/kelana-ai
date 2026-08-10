"""
KelanaAI - Trip Summary Generator (Console Version)
Sesi 1: Building the First Feature of KelanaAI
"""

def print_trip_summary(destination: str, country: str, days: int, budget: float, currency: str, travel_month: str) -> None:
    """
    Mencetak ringkasan rencana perjalanan dengan format visual yang rapi dan profesional.
    """
    # Formatting budget dengan separator ribuan dan 2 digit desimal
    formatted_budget = f"{budget:,.2f}"
    
    print("\n" + "=" * 40)
    print("           ✈️  KELANA AI  ✈️           ")
    print("     Your Personal Travel Companion     ")
    print("=" * 40)
    print(f" Destination  : {destination.strip().title()}")
    print(f" Country      : {country.strip().title()}")
    print(f" Days         : {days} Day(s)")
    print(f" Budget       : {formatted_budget} {currency.strip().upper()}")
    print(f" Currency     : {currency.strip().upper()}")
    print(f" Travel Month : {travel_month.strip().title()}")
    print("=" * 40)
    print("Status: Ready to plan your itinerary!\n")

def get_integer_input(prompt_text: str) -> int:
    """Fungsi helper untuk menjamin validasi input integer (Jumlah Hari)."""
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
    """Fungsi helper untuk menjamin validasi input float (Estimasi Anggaran)."""
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
    print("\n--- 📝 Selamat Datang di KelanaAI Trip Planner Setup ---")
    
    # a. Input Interaktif Pengguna
    destination = input("Masukkan Destinasi Wisata : ")
    country = input("Masukkan Negara           : ")
    days = get_integer_input("Masukkan Durasi (Hari)    : ")
    budget = get_float_input("Masukkan Total Budget     : ")
    currency = input("Masukkan Mata Uang        : ")
    travel_month = input("Masukkan Bulan Perjalanan : ")

    # b. Memanggil Fungsi Formatting Output
    print_trip_summary(
        destination=destination,
        country=country,
        days=days,
        budget=budget,
        currency=currency,
        travel_month=travel_month
    )

if __name__ == "__main__":
    main()