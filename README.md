# 🚲 Bike Sharing Dashboard

## 📌 Deskripsi Proyek
Dashboard interaktif ini dibuat untuk menganalisis data penyewaan sepeda berdasarkan musim, cuaca, dan waktu. Dengan fitur interaktif yang memungkinkan pengguna untuk menyesuaikan rentang waktu dan kondisi cuaca, pengguna dapat memperoleh wawasan yang lebih dalam mengenai tren penyewaan sepeda.

## 📊 Fitur Utama
- **Visualisasi Tren Penyewaan** berdasarkan hari, musim, dan kondisi cuaca.
- **Filter Interaktif** untuk memilih rentang tanggal, musim, dan kondisi cuaca tertentu.
- **Grafik Estetik** dengan anotasi jumlah penyewaan dalam ribuan untuk mempermudah analisis.

## 📂 Dataset
Dataset yang digunakan berasal dari **Bike Sharing Dataset**, yang mencakup informasi penyewaan sepeda dari tahun 2011-2012.

### **Fitur Data**
- **Tanggal (`dteday`)**: Format datetime dari data penyewaan.
- **Musim (`season`)**: Dikategorikan menjadi Spring, Summer, Fall, dan Winter.
- **Kondisi Cuaca (`weathersit`)**: Clear/Few Clouds, Mist/Cloudy, Light Snow/Rain, dan Heavy Rain/Snow.
- **Jumlah Penyewaan Sepeda (`cnt`)**: Total jumlah sepeda yang disewa setiap harinya.

## 🔍 Langkah-langkah Analisis
1. **Menentukan pertanyaan bisnis**
   - Mengidentifikasi faktor yang memengaruhi penyewaan sepeda.
   - Mengamati tren penyewaan berdasarkan musim dan cuaca.
2. **Data Wrangling**
   - Mengumpulkan, membersihkan, dan menyiapkan data untuk analisis.
3. **Exploratory Data Analysis (EDA)**
   - Mengeksplorasi pola penyewaan sepeda berdasarkan variabel tertentu.
4. **Visualisasi Data & Explanatory Analysis**
   - Membuat grafik dan diagram untuk mendukung analisis data.
5. **Analisis Lanjutan**
   - Menemukan pola musiman dalam penyewaan sepeda.
6. **Membuat Dashboard Interaktif dengan Streamlit**
   - Membangun tampilan interaktif yang memungkinkan pengguna menganalisis data secara visual.

## 🛠 Instalasi
Untuk menjalankan proyek ini di lokal, ikuti langkah-langkah berikut:

### **1️⃣ Clone repository**
```bash
git clone https://github.com/username/repository.git
cd repository
```

### **2️⃣ Install dependensi**
Pastikan Anda memiliki **Python** dan **pip** terinstal, lalu jalankan:
```bash
pip install -r requirements.txt
```

### **3️⃣ Jalankan aplikasi dengan Streamlit**
```bash
streamlit run dashboard/dashboard.py
```

## 📊 Cara Menggunakan Dashboard
1. Pilih **rentang tanggal** dari sidebar.
2. Pilih **musim** dan **kondisi cuaca** untuk memfilter data.
3. Gunakan **tema interaktif** untuk mengubah tampilan dashboard.
4. Analisis tren penyewaan berdasarkan musim dan kondisi cuaca.


