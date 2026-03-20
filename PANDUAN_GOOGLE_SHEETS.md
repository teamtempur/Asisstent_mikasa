# 📊 Panduan Setup Google Sheets API

Panduan lengkap untuk mengkonfigurasi Google Sheets API agar bot dapat terhubung dengan spreadsheet Anda.

## 🎯 Ringkasan Langkah

1. Buat Project di Google Cloud Console
2. Aktifkan Google Sheets API dan Google Drive API
3. Buat Service Account
4. Download Credentials (JSON)
5. Share Spreadsheet dengan Service Account

---

## 📋 Langkah-langkah Detail

### 1. Buat Project di Google Cloud Console

1. Buka [Google Cloud Console](https://console.cloud.google.com/)
2. Klik dropdown project di bagian atas (sebelah "Google Cloud Platform")
3. Klik **"New Project"**
4. Masukkan nama project, contoh: `telegram-bot-tuktuk`
5. Klik **"Create"**
6. Tunggu hingga project selesai dibuat, lalu pilih project tersebut

---

### 2. Aktifkan API yang Diperlukan

#### Aktifkan Google Sheets API:

1. Di menu kiri, klik **"APIs & Services"** > **"Library"**
2. Cari **"Google Sheets API"**
3. Klik pada hasil pencarian
4. Klik tombol **"Enable"**

#### Aktifkan Google Drive API:

1. Kembali ke **"APIs & Services"** > **"Library"**
2. Cari **"Google Drive API"**
3. Klik pada hasil pencarian
4. Klik tombol **"Enable"**

> **Catatan:** Google Drive API diperlukan agar bot dapat mengakses spreadsheet yang dibuat di Google Drive Anda.

---

### 3. Buat Service Account

Service Account adalah "akun robot" yang akan digunakan bot untuk mengakses Google Sheets.

1. Di menu kiri, klik **"APIs & Services"** > **"Credentials"**
2. Klik tombol **"+ Create Credentials"** di bagian atas
3. Pilih **"Service Account"**

#### Langkah 1: Service Account Details

- **Service account name:** `telegram-bot-tuktuk` (atau nama lain)
- **Service account ID:** akan otomatis terisi
- **Description:** `Service account untuk bot Telegram claim tuk-tuk`
- Klik **"Create and Continue"**

#### Langkah 2: Grant this service account access to project (Opsional)

- Role: Biarkan kosong atau pilih **"Editor"**
- Klik **"Continue"**

#### Langkah 3: Grant users access to this service account (Opsional)

- Biarkan kosong
- Klik **"Done"**

---

### 4. Buat dan Download Credentials (JSON)

1. Di halaman **"Credentials"**, klik pada **Service Account** yang baru dibuat
2. Pergi ke tab **"Keys"**
3. Klik **"Add Key"** > **"Create New Key"**
4. Pilih format **"JSON"**
5. Klik **"Create"**
6. File JSON akan otomatis terdownload ke komputer Anda
7. **PENTING:** Rename file tersebut menjadi `credentials.json`
8. Pindahkan file `credentials.json` ke folder bot (sejajar dengan `bot.py`)

> **⚠️ PERINGATAN KEAMANAN:**
> - File `credentials.json` berisi kunci akses pribadi
> - **JANGAN** upload file ini ke GitHub atau bagikan ke orang lain
> - File ini sudah dimasukkan di `.gitignore` agar tidak ter-commit

---

### 5. Buat Spreadsheet Google Sheets

1. Buka [Google Sheets](https://sheets.google.com)
2. Klik tombol **"+ Blank"** untuk membuat spreadsheet baru
3. Beri nama spreadsheet: `Claim TukTuk` (atau nama lain sesuai config)
4. **Catat/kopi email Service Account** dari Google Cloud Console:
   - Buka [Google Cloud Console](https://console.cloud.google.com/) > IAM & Admin > Service Accounts
   - Email akan terlihat seperti: `nama-service@project-id.iam.gserviceaccount.com`

---

### 6. Share Spreadsheet dengan Service Account

1. Di spreadsheet Google Sheets, klik tombol **"Share"** (kanan atas)
2. Di kolom "Add people and groups", paste **email Service Account**
3. Ubah permission dari **"Viewer"** menjadi **"Editor"**
4. Klik **"Send"**

> **Catatan:** Service Account tidak akan menerima email notifikasi, itu normal.

---

## ✅ Verifikasi Setup

Untuk memastikan setup berhasil, jalankan bot dan coba command `/rekapan`:

```bash
python bot.py
```

Jika tidak ada error dan bot merespons, berarti setup Google Sheets berhasil! 🎉

---

## 🔧 Troubleshooting

### Error: `FileNotFoundError: credentials.json`

**Solusi:**
- Pastikan file `credentials.json` ada di folder yang sama dengan `bot.py`
- Pastikan nama file persis `credentials.json` (bukan `credentials (1).json`)

### Error: `SpreadsheetNotFound`

**Solusi:**
- Pastikan nama spreadsheet di `config.py` sama persis dengan nama di Google Sheets
- Pastikan spreadsheet sudah di-share dengan email Service Account
- Pastikan permissionnya adalah **"Editor"**, bukan "Viewer"

### Error: `Permission denied`

**Solusi:**
- Pastikan Google Sheets API dan Google Drive API sudah diaktifkan
- Pastikan Service Account memiliki permission yang benar
- Coba hapus dan buat Service Account baru

### Error: `Invalid credentials`

**Solusi:**
- Pastikan file `credentials.json` tidak corrupt
- Coba download ulang credentials dari Google Cloud Console
- Pastikan tidak ada karakter tambahan di file JSON

---

## 📚 Referensi

- [Google Sheets API Documentation](https://developers.google.com/sheets/api)
- [Google Cloud Console](https://console.cloud.google.com/)
- [gspread Documentation](https://docs.gspread.org/)

---

Jika masih mengalami kendala, silakan buat issue di repository atau hubungi developer.
