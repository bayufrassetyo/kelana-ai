# 📋 KelanaAI - Development Tasks & Roadmap

Dokumen ini mencatat riwayat pengerjaan tugas (_checklist_ pengerjaan) dari Sesi 1 hingga Sesi 3.

---

## 🎯 Sesi 1: Trip Summary Generator (Console App)

- [x] **Setup Repositori & Struktur Awal**: Membuat struktur folder dasar `backend` dan `frontend/.gitkeep`.
- [x] **Input Handling**: Mengumpulkan parameter awal dari pengguna (Destination, Days, Budget, Currency, Travel Month).
- [x] **Summary Output**: Menampilkan ringkasan rencana perjalanan terstruktur ke konsol/terminal.
- [x] **Tagging Sesi 1**: Membuat tag `v0.1.0` / `session-1`.

---

## 🎯 Sesi 2: Layered Architecture & Recommendation Engine

- [x] **Separation of Concerns (SoC)**:
  - Memisahkan _Presentation Layer_ (`main.py`) dan _Business Logic Layer_ (`services/trip_service.py`).
- [x] **Business Logic Implementation (`trip_service.py`)**:
  - Implementasi `get_trip_category()` untuk pengelompokkan jenis trip (_Backpacker_, _Standard_, _Luxury_).
  - Implementasi `get_travel_session()` untuk menentukan musim perjalanan berdasarkan bulan.
  - Implementasi `calculate_daily_budget()` untuk alokasi anggaran harian.
  - Implementasi `get_recommended_places()` menggunakan koleksi data `list` dan perulangan `for`.
- [x] **Input Validation & Formatting (`main.py`)**:
  - Menambahkan _error handling_ (`try-except`) untuk input numerik (Days & Budget).
  - Format tampilan output dengan _f-strings_.
- [x] **Repository Cleanup & Tagging**:
  - Membuat `.gitignore` untuk menyaring folder cache `__pycache__`.
  - Mengunci rilis dengan tag `session-2`.

---

## 🎯 Sesi 3: Teaching KelanaAI to Communicate (REST API dengan FastAPI)

- [x] **Environment & Dependency Setup**:
  - Menginstal `fastapi` dan `uvicorn`.
- [x] **Refactoring Presentation Layer (`main.py`)**:
  - Mengubah konsol interaktif menjadi Web API menggunakan FastAPI.
  - Membuat Pydantic Model (`TripRequest`) untuk memvalidasi _request body_ (`destination`, `days`, `budget`).
  - Mengintegrasikan kembali fungsi `trip_service.py` tanpa mengubah logika bisnisnya.
- [x] **Endpoint Implementation**:
  - `GET /` → Pesan sambutan API (`{"message": "Welcome to KelanaAI"}`).
  - `GET /health` → Endpoint status kesehatan server (`{"status": "OK"}`).
  - `POST /api/v1/trips` → Endpoint kalkulasi _daily budget_ & kategori trip.
- [x] **Homework Extension**:
  - `GET /api/v1/recommendations` → Mengembalikan list rekomendasi tempat wisata.
  - `GET /api/v1/transportations` → Mengembalikan list pilihan moda transportasi.
- [x] **API Testing & Documentation**:
  - Pengujian _endpoint_ berhasil 100% via Swagger UI (`http://localhost:8000/docs`).
  - Pembaruan dokumen `README.md` dan `TASKS.md`.
- [x] **Release Management**:
  - Mengunci rilis Sesi 3 dengan tag `session-3`.

---
