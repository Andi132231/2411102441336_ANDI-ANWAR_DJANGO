# Django Web Project

Selamat datang di proyek Django ini!  
Website ini adalah aplikasi web sederhana namun fungsional yang memiliki halaman utama serta dashboard interaktif dengan visualisasi data.

---

## Fitur Website

🔹 **Beranda (Home)**  
&nbsp;&nbsp;&nbsp;&nbsp;Halaman awal sebagai titik masuk pengguna.

🔹 **Dashboard**  
&nbsp;&nbsp;&nbsp;&nbsp;Menampilkan grafik, data interaktif, dan manajemen informasi secara real-time.

---

## Cara Menjalankan Proyek

```bash
# 1. Masuk ke direktori proyek
cd nama_folder

```bash
# 2. Buat virtual environment
py -m venv .venv

```bash
# 3. Aktifkan virtual environment
.venv\Scripts\activate       

```bash
# 4. Install Django
pip install django

```bash
# 5. Generate dan jalankan migrasi database
python manage.py makemigrations
python manage.py migrate

```bash
# 6. Jalankan server Django
python manage.py runserver

```bash
# 7. Akses website di browser
# Buka alamat berikut:
# http://127.0.0.1:8000/
