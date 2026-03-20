# 📦 Panduan Instalasi Bot Telegram Claim TukTuk

Panduan lengkap untuk menginstall dan menjalankan bot Telegram untuk pencatatan claim tuk-tuk.

## 📋 Prasyarat

Sebelum memulai, pastikan Anda memiliki:

- ✅ Python 3.8 atau lebih baru
- ✅ Akun Telegram
- ✅ Akun Google (untuk Google Sheets)
- ✅ Koneksi internet

---

## 🚀 Cara Instalasi (Windows)

### 1. Download dan Extract

1. Download repository ini sebagai ZIP
2. Extract ke folder pilihan Anda
3. Buka folder hasil extract

### 2. Install Python

Jika belum install Python:

1. Download dari [python.org](https://python.org)
2. Saat install, **centang "Add Python to PATH"**
3. Klik Install Now

### 3. Setup Bot Telegram

1. Buka Telegram, cari [@BotFather](https://t.me/BotFather)
2. Kirim `/newbot`
3. Masukkan nama bot (contoh: `Claim TukTuk Bot`)
4. Masukkan username bot (contoh: `claimtuktuk_bot`)
5. Simpan **Bot Token** yang diberikan

### 4. Setup Google Sheets API

Ikuti panduan lengkap di [PANDUAN_GOOGLE_SHEETS.md](PANDUAN_GOOGLE_SHEETS.md)

Ringkasnya:
1. Buat project di [Google Cloud Console](https://console.cloud.google.com/)
2. Aktifkan Google Sheets API dan Google Drive API
3. Buat Service Account dan download credentials JSON
4. Rename file menjadi `credentials.json`
5. Pindahkan ke folder bot

### 5. Konfigurasi Bot

**Pilih salah satu cara:**

#### Cara A: Menggunakan File .env (Direkomendasikan)

1. Copy file `.env.example` menjadi `.env`
2. Buka file `.env` dengan text editor
3. Isi konfigurasi:
   ```
   TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxyz
   ```
4. Save file

#### Cara B: Menggunakan config.py

1. Buka file `config.py`
2. Ganti `YOUR_BOT_TOKEN_HERE` dengan token bot Anda:
   ```python
   TELEGRAM_BOT_TOKEN = "123456789:ABCdefGHIjklMNOpqrSTUvwxyz"
   ```
3. Save file

### 6. Install Dependencies

Buka Command Prompt atau PowerShell di folder bot, lalu jalankan:

```bash
pip install -r requirements.txt
```

### 7. Jalankan Bot

**Cara 1: Menggunakan run.bat (Direkomendasikan)**

```bash
run.bat
```

**Cara 2: Manual**

```bash
python bot.py
```

**Cara 3: Menggunakan start.bat**

```bash
start.bat
```

---

## 🍎 Cara Instalasi (Mac/Linux)

### 1. Download dan Extract

```bash
# Download repository
git clone https://github.com/yourusername/telegram-bot-tuktuk.git

# Atau download ZIP dan extract
# Lalu masuk ke folder
cd telegram-bot-tuktuk
```

### 2. Install Python (jika belum)

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
```

**Mac (dengan Homebrew):**
```bash
brew install python3
```

### 3. Setup Bot Telegram

Sama dengan langkah Windows (lihat di atas)

### 4. Setup Google Sheets API

Sama dengan langkah Windows, lihat [PANDUAN_GOOGLE_SHEETS.md](PANDUAN_GOOGLE_SHEETS.md)

### 5. Konfigurasi Bot

```bash
# Copy file .env
cp .env.example .env

# Edit file .env
nano .env  # atau gunakan editor favorit Anda
```

Isi konfigurasi:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

### 6. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 7. Jalankan Bot

**Cara 1: Menggunakan run.sh (Direkomendasikan)**

```bash
chmod +x run.sh
./run.sh
```

**Cara 2: Manual**

```bash
python3 bot.py
```

**Cara 3: Menggunakan start.sh**

```bash
chmod +x start.sh
./start.sh
```

---

## 🐳 Cara Instalasi (Docker)

Jika Anda menggunakan Docker:

### 1. Buat Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
```

### 2. Build dan Run

```bash
# Build image
docker build -t telegram-bot-tuktuk .

# Run container
docker run -d --name tuktuk-bot \
  -e TELEGRAM_BOT_TOKEN=your_token_here \
  -v $(pwd)/credentials.json:/app/credentials.json \
  telegram-bot-tuktuk
```

---

## ☁️ Cara Deploy (Heroku)

### 1. Install Heroku CLI

Download dan install dari [devcenter.heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

### 2. Login dan Buat App

```bash
heroku login
heroku create nama-app-anda
```

### 3. Setup Environment Variables

```bash
heroku config:set TELEGRAM_BOT_TOKEN=your_token_here
heroku config:set GOOGLE_SHEETS_CREDENTIALS_FILE=credentials.json
```

### 4. Deploy

```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### 5. Scale Worker

```bash
heroku ps:scale worker=1
```

---

## 🔧 Troubleshooting Instalasi

### Error: `pip is not recognized`

**Solusi:**
- Pastikan Python sudah ditambahkan ke PATH
- Coba install ulang Python dengan centang "Add Python to PATH"

### Error: `ModuleNotFoundError`

**Solusi:**
```bash
# Install ulang dependencies
pip install -r requirements.txt --force-reinstall
```

### Error: `Permission denied` (Mac/Linux)

**Solusi:**
```bash
# Tambahkan permission execute
chmod +x run.sh
chmod +x start.sh
```

### Error: `credentials.json not found`

**Solusi:**
- Pastikan file `credentials.json` ada di folder yang sama dengan `bot.py`
- Pastikan nama file persis `credentials.json`

---

## ✅ Verifikasi Instalasi

Setelah bot berjalan, coba kirim pesan ke bot di Telegram:

1. Cari bot Anda di Telegram (username yang Anda buat)
2. Kirim `/start`
3. Jika bot merespons dengan menu utama, berarti instalasi berhasil! 🎉

---

## 🔄 Update Bot

Untuk update ke versi terbaru:

```bash
# Backup file .env dan credentials.json
cp .env .env.backup
cp credentials.json credentials.json.backup

# Download versi terbaru
# Extract dan replace file

# Restore backup
cp .env.backup .env
cp credentials.json.backup credentials.json

# Update dependencies
pip install -r requirements.txt --upgrade
```

---

## 📞 Butuh Bantuan?

Jika mengalami kendala:

1. Cek [PANDUAN_GOOGLE_SHEETS.md](PANDUAN_GOOGLE_SHEETS.md) untuk masalah Google Sheets
2. Cek [README.md](README.md) untuk informasi umum
3. Buat issue di repository

---

Selamat menggunakan Bot Telegram Claim TukTuk! 🛺
