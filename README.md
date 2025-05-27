# 🎓 Prediksi Kelulusan Mahasiswa

Sistem ini memprediksi apakah seorang mahasiswa akan **lulus tepat waktu** atau tidak berdasarkan:
- **IPK**
- **Jumlah Kehadiran**
- **Jumlah Keikutsertaan dalam Organisasi**

Model dibuat menggunakan `scikit-learn`, disediakan API menggunakan `Flask`, dan dashboard monitoring real-time menggunakan `Streamlit`.

---

## 🚀 Fitur Utama

✅ Prediksi kelulusan dengan model Logistic Regression  
✅ API endpoint POST `/predict` untuk menerima input mahasiswa  
✅ Logging otomatis ke file  
✅ Dashboard real-time interaktif berbasis `Streamlit`  

---

## 🔧 Instalasi & Setup Lengkap

Ikuti langkah-langkah berikut **jika laptop belum menginstall environment** sama sekali:

### 1. 📥 Install Python

Download dan install [Python untuk Windows](https://www.python.org/downloads/windows)  
> **Add Python to PATH** saat instalasi!

---

### 2. 💼 Clone Repo & Masuk Folder Proyek

```bash
git clone https://github.com/username/prediksi-kelulusan.git
cd prediksi-kelulusan
```

---

### 3. 🧪 (Opsional) Buat Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 4. 📦 Install Semua Dependensi

```bash
pip install -r requirements.txt
```

**Atau manual jika belum punya file `requirements.txt`:**

```bash
pip install scikit-learn flask streamlit matplotlib pandas streamlit-autorefresh joblib
```

---

### 5. 🧠 Melatih Model (Opsional)

```bash
python kelulusan.py
```

---

### 6. 🔥 Menjalankan Flask API

```bash
python app2.py
```

> Default berjalan di: `http://127.0.0.1:5000`

---

### 7. 🧪 Uji Coba Endpoint Prediksi

Kirim data via `curl`, Postman, atau tools lainnya:

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d "{\"Nama\":\"Andi\",\"IPK\":3.9,\"Kehadiran\":120,\"Organisasi\":2}"
```

---

### 8. 📊 Menjalankan Streamlit Dashboard

```bash
streamlit run dashboard.py
```

> Akses dashboard di browser: `http://localhost:8501`

---

## 🎥 Demo

📺 _Coming Soon!_
