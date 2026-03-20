# 🚀 Quick Start - Bot Telegram Claim TukTuk

Panduan cepat untuk menjalankan bot dalam 5 menit!

---

## ⚡ 3 Langkah Cepat

### 1️⃣ Setup Bot Telegram (2 menit)

1. Buka Telegram, cari [@BotFather](https://t.me/BotFather)
2. Kirim `/newbot`
3. Masukkan nama bot: `Claim TukTuk Bot`
4. Masukkan username: `claimtuktuk_bot` (harus unik)
5. **Simpan token yang diberikan!**

### 2️⃣ Setup Google Sheets (2 menit)

1. Buka [Google Sheets](https://sheets.google.com), buat spreadsheet baru
2. Beri nama: `Claim TukTuk`
3. Buka [Google Cloud Console](https://console.cloud.google.com/)
4. Buat project baru → Aktifkan **Google Sheets API** dan **Google Drive API**
5. **Credentials** → **Create Credentials** → **Service Account**
6. Tab **Keys** → **Add Key** → **Create New Key** → **JSON**
7. Download file JSON, rename jadi `credentials.json`
8. Share spreadsheet dengan email service account (contoh: `nama@project.iam.gserviceaccount.com`)

> 📖 Panduan lengkap: [PANDUAN_GOOGLE_SHEETS.md](PANDUAN_GOOGLE_SHEETS.md)

### 3️⃣ Jalankan Bot (1 menit)

**Windows:**
```bash
# 1. Edit config.py, masukkan token bot
# 2. Jalankan
pip install -r requirements.txt
python bot.py
```

**Mac/Linux:**
```bash
# 1. Edit config.py, masukkan token bot
# 2. Jalankan
pip3 install -r requirements.txt
python3 bot.py
```

---

## ✅ Verifikasi

1. Cari bot Anda di Telegram
2. Kirim `/start`
3. Jika bot merespons, **SUKSES!** 🎉

---

## 📋 Command Bot

| Command | Fungsi |
|---------|--------|
| `/start` | Mulai bot |
| `/tambah` | Tambah claim baru |
| `/rekapan` | Lihat ringkasan |
| `/status` | Cek status per orang |
| `/lunas` | Lihat yang sudah lunas |
| `/belumlunas` | Lihat yang belum lunas |
| `/help` | Bantuan |

---

## ❓ Masalah Umum

| Masalah | Solusi |
|---------|--------|
| `credentials.json not found` | Pastikan file ada di folder yang sama dengan bot.py |
| `SpreadsheetNotFound` | Pastikan nama spreadsheet sama persis dengan config |
| `Permission denied` | Pastikan spreadsheet di-share dengan email service account |

---

## 📚 Dokumentasi Lengkap

- [README.md](README.md) - Dokumentasi utama
- [INSTALL.md](INSTALL.md) - Panduan instalasi detail
- [PANDUAN_GOOGLE_SHEETS.md](PANDUAN_GOOGLE_SHEETS.md) - Setup Google Sheets

---

**Selamat menggunakan bot!** 🛺
