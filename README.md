# ⚡ Django Web Project

Selamat datang di proyek Django ini! Proyek ini adalah website sederhana namun fungsional yang memiliki fitur halaman utama dan dashboard dengan visualisasi data.

---

## 📝 Fitur Website

- **🏠 Beranda (Home)**  
  Halaman utama sebagai titik awal navigasi pengguna.

- **📊 Dashboard**  
  Menyajikan laporan grafis, manajemen informasi, dan data dalam antarmuka yang interaktif serta responsif.

---

## 🔧 Cara Menjalankan Proyek

### ⚙️ Persiapan Awal

💡 Website ini mencakup:
- **HOME** – Tampilan awal sebagai halaman pengenalan.
- **DASHBOARD** – Visualisasi data dan pengelolaan informasi dinamis.

### 🪄 Langkah-langkah:

1. **Buka Command Prompt (CMD)**
   ```bash
   Win + R → ketik `cmd` → tekan Enter
Masuk ke Direktori Proyek

bash
Copy
Edit
cd nama_folder
Buat Virtual Environment

bash
Copy
Edit
py -m venv .venv
Aktifkan Virtual Environment

bash
Copy
Edit
.venv\Scripts\activate
Install Django

bash
Copy
Edit
pip install django
Generate Migration

bash
Copy
Edit
python manage.py makemigrations
Migrate Database

bash
Copy
Edit
python manage.py migrate
Jalankan Server

bash
Copy
Edit
python manage.py runserver
🌐 Akses Website
Buka browser dan akses:

cpp
Copy
Edit
http://127.0.0.1:8000/