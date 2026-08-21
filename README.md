# ✈️ KelanaAI - AI Travel Planner

KelanaAI adalah aplikasi perencanaan perjalanan (_Travel Planner_) pintar berbasis Python, FastAPI, dan PostgreSQL.

---

## 📌 Fitur & Riwayat Pengembangan

### Sesi 1: Trip Summary Generator (Console App)

- Aplikasi konsol interaktif berbasis Python untuk mengumpulkan parameter awal rencana perjalanan dan menghasilkan ringkasan yang terstruktur.

### Sesi 2: Interactive Console Interface & Recommendation Engine

- **Layered Architecture:** Pemisahan _Presentation Layer_ (`main.py`) dan _Business Logic Layer_ (`services/trip_service.py`).
- **Kategori Perjalanan:** Penentuan otomatis kategori (_Backpacker_, _Standard_, _Luxury_) berdasarkan total anggaran.
- **Kategori Musim:** Penentuan musim (_Peak Season_, _Holiday Season_, _Regular Season_) berdasarkan bulan perjalanan.
- **Kalkulasi Anggaran Harian:** Perhitungan otomatis estimasi pengeluaran per hari (`budget / days`).
- **Engine Rekomendasi Tempat:** Rekomendasi tempat wisata berbasis koleksi tipe data _list_ dan perulangan.

### Sesi 3: Teaching KelanaAI to Communicate (REST API dengan FastAPI)

- **Web Presentation Layer:** Mentransformasi aplikasi konsol menjadi REST API interaktif berbasis FastAPI dan Uvicorn.
- **Data Validation:** Menggunakan Pydantic (`TripRequest`) untuk memvalidasi _request body_.
- **Separation of Concerns:** Memanfaatkan kembali seluruh fungsi bisnis dari `services/trip_service.py` tanpa mengubah _logic_ di dalamnya.
- **Homework Endpoints (GET Lists):** Penambahan endpoint `/api/v1/recommendations` dan `/api/v1/transportations`.
- **Interactive Documentation:** Mendukung pengujian _endpoint_ otomatis via Swagger UI (`/docs`).

### Sesi 4: Database Persistence & Full CRUD Operations

- **Database Integration:** Mengintegrasikan database **PostgreSQL** berbasis Docker Container dengan SQLAlchemy ORM.
- **Data Modeling & Schemas:** Pembuatan database model (`Trip`) dan schema Pydantic (`TripCreate`, `TripUpdate`, `TripResponse`).
- **Full CRUD Endpoints:**
  - `POST /api/v1/trips` → Membuat dan menyimpan rencana perjalanan ke PostgreSQL.
  - `GET /api/v1/trips` → Menampilkan daftar seluruh data perjalanan dari database.
  - `GET /api/v1/trips/{trip_id}` → Menampilkan detail rencana perjalanan spesifik.
  - `PUT /api/v1/trips/{trip_id}` → Memperbarui anggaran perjalanan dan menghitung ulang alokasi harian serta kategori.
  - `DELETE /api/v1/trips/{trip_id}` → Menghapus data perjalanan dari database.
- **Environment Variable Management:** Mengamankan kredensial database menggunakan berkas `.env` dan `python-dotenv`.

---

## 🛠️ Struktur Proyek

```text
kelana-ai/
├── .env
├── .gitignore
├── README.md
├── TASKS.md
├── requirements.txt
├── backend/
│   ├── database.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── trip.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── trip.py
│   └── services/
│       ├── __init__.py
│       └── trip_service.py
└── frontend/
    └── .gitkeep
```
