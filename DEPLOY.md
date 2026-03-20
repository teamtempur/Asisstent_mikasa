# 🚀 Panduan Deployment - Bot Telegram Claim TukTuk

Panduan lengkap untuk deploy bot ke berbagai platform.

---

## 📋 Daftar Platform

| Platform | Difficulty | Cost | Recommended |
|----------|------------|------|-------------|
| [Heroku](#heroku) | Easy | Free | ⭐⭐⭐ |
| [Railway](#railway) | Easy | Free | ⭐⭐⭐ |
| [PythonAnywhere](#pythonanywhere) | Easy | Free | ⭐⭐ |
| [VPS/Dedicated Server](#vps) | Medium | Paid | ⭐⭐ |
| [Docker](#docker) | Medium | Varies | ⭐⭐ |
| [Raspberry Pi](#raspberry-pi) | Medium | One-time | ⭐ |

---

## Heroku

### 1. Setup

```bash
# Install Heroku CLI
# Download dari: https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Buat app
heroku create nama-app-anda
```

### 2. Buat File Konfigurasi

**Procfile** (tanpa extension):
```
worker: python bot.py
```

**runtime.txt**:
```
python-3.11.0
```

### 3. Setup Environment Variables

```bash
heroku config:set TELEGRAM_BOT_TOKEN=your_token_here
heroku config:set GOOGLE_SHEETS_CREDENTIALS_FILE=credentials.json
heroku config:set SPREADSHEET_NAME=Claim TukTuk
```

### 4. Deploy

```bash
# Commit
git add .
git commit -m "Deploy to Heroku"

# Push
git push heroku main

# Scale worker
heroku ps:scale worker=1
```

### 5. Monitor

```bash
# Lihat log
heroku logs --tail

# Status
heroku ps
```

---

## Railway

### 1. Setup

1. Daftar di [railway.app](https://railway.app)
2. Connect dengan GitHub repository Anda
3. Buat project baru

### 2. Environment Variables

1. Buka dashboard Railway
2. Pergi ke tab **Variables**
3. Tambahkan:
   - `TELEGRAM_BOT_TOKEN`
   - `GOOGLE_SHEETS_CREDENTIALS_FILE`
   - `SPREADSHEET_NAME`

### 3. Deploy

Railway akan otomatis deploy saat Anda push ke GitHub.

---

## PythonAnywhere

### 1. Setup

1. Daftar di [pythonanywhere.com](https://pythonanywhere.com)
2. Pilih plan (free plan tersedia)
3. Buka **Consoles** → **Bash**

### 2. Install

```bash
# Clone repository
git clone https://github.com/yourusername/telegram-bot-tuktuk.git
cd telegram-bot-tuktuk

# Buat virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Konfigurasi

```bash
# Edit config.py atau buat .env
nano config.py

# Upload credentials.json
# Gunakan menu Files di PythonAnywhere
```

### 4. Jalankan sebagai Always-On Task

1. Buka **Tasks**
2. Buat task baru:
   ```
   cd ~/telegram-bot-tuktuk && source venv/bin/activate && python bot.py
   ```
3. Klik **Create**

---

## VPS/Dedicated Server

### 1. Setup Server

```bash
# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install Python dan pip
sudo apt-get install python3 python3-pip python3-venv -y

# Install git
sudo apt-get install git -y
```

### 2. Clone dan Install

```bash
# Clone repository
git clone https://github.com/yourusername/telegram-bot-tuktuk.git
cd telegram-bot-tuktuk

# Buat virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Konfigurasi

```bash
# Edit config
nano config.py

# Atau buat .env
nano .env
```

### 4. Jalankan dengan Systemd

Buat service file:

```bash
sudo nano /etc/systemd/system/tuktuk-bot.service
```

Isi dengan:

```ini
[Unit]
Description=Telegram Bot Claim TukTuk
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/home/your_username/telegram-bot-tuktuk
Environment=PATH=/home/your_username/telegram-bot-tuktuk/venv/bin
ExecStart=/home/your_username/telegram-bot-tuktuk/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable dan start service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable tuktuk-bot
sudo systemctl start tuktuk-bot

# Cek status
sudo systemctl status tuktuk-bot

# Lihat log
sudo journalctl -u tuktuk-bot -f
```

### 5. Jalankan dengan PM2 (Alternatif)

```bash
# Install PM2
sudo npm install -g pm2

# Jalankan bot
pm2 start bot.py --name tuktuk-bot --interpreter python3

# Save config
pm2 save
pm2 startup

# Monitor
pm2 monit
pm2 logs tuktuk-bot
```

---

## Docker

### 1. Buat Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Run bot
CMD ["python", "bot.py"]
```

### 2. Buat docker-compose.yml (Opsional)

```yaml
version: '3.8'

services:
  bot:
    build: .
    container_name: tuktuk-bot
    restart: always
    environment:
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
      - GOOGLE_SHEETS_CREDENTIALS_FILE=credentials.json
    volumes:
      - ./credentials.json:/app/credentials.json
```

### 3. Build dan Run

```bash
# Build image
docker build -t telegram-bot-tuktuk .

# Run container
docker run -d \
  --name tuktuk-bot \
  -e TELEGRAM_BOT_TOKEN=your_token_here \
  -v $(pwd)/credentials.json:/app/credentials.json \
  telegram-bot-tuktuk

# Atau dengan docker-compose
docker-compose up -d
```

### 4. Monitor

```bash
# Lihat log
docker logs -f tuktuk-bot

# Status
docker ps
```

---

## Raspberry Pi

### 1. Setup

```bash
# Update
sudo apt-get update
sudo apt-get upgrade -y

# Install Python
sudo apt-get install python3 python3-pip python3-venv -y
```

### 2. Install Bot

```bash
# Clone
git clone https://github.com/yourusername/telegram-bot-tuktuk.git
cd telegram-bot-tuktuk

# Virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Autostart dengan Cron

```bash
# Edit crontab
crontab -e

# Tambahkan baris berikut
@reboot cd /home/pi/telegram-bot-tuktuk && source venv/bin/activate && python bot.py
```

### 4. Atau dengan Systemd

Sama dengan [VPS/Dedicated Server](#vps) di atas.

---

## 🔧 Troubleshooting Deployment

### Bot tidak berjalan

**Cek log:**
```bash
# Heroku
heroku logs --tail

# Systemd
sudo journalctl -u tuktuk-bot -f

# Docker
docker logs tuktuk-bot

# PM2
pm2 logs tuktuk-bot
```

### Error Google Sheets

- Pastikan `credentials.json` ada dan valid
- Pastikan environment variables sudah di-set
- Cek permission file

### Bot terus restart

- Cek error di log
- Pastikan token bot valid
- Pastikan tidak ada instance lain yang berjalan

---

## 📊 Monitoring

### Heroku

```bash
heroku logs --tail
heroku ps
```

### Systemd

```bash
sudo systemctl status tuktuk-bot
sudo journalctl -u tuktuk-bot -f
```

### PM2

```bash
pm2 status
pm2 monit
pm2 logs
```

### Docker

```bash
docker ps
docker logs -f tuktuk-bot
docker stats
```

---

## 💰 Perbandingan Biaya

| Platform | Free Tier | Paid Tier | Keterangan |
|----------|-----------|-----------|------------|
| Heroku | ✅ | $7/month | Free tier sleep after 30 mins |
| Railway | ✅ | $5/month | Free tier tersedia |
| PythonAnywhere | ✅ | $5/month | Always-on task limited |
| VPS | ❌ | $5-20/month | Full control |
| Docker | Varies | Varies | Depends on hosting |
| Raspberry Pi | ✅ | One-time | Hardware cost |

---

## 🎯 Rekomendasi

### Untuk Pemula
- **Heroku** atau **Railway** - Mudah setup, free tier tersedia

### Untuk Production
- **VPS** - Full control, reliable
- **PythonAnywhere** - Simple, managed

### Untuk Development
- **Local** - Test dulu sebelum deploy
- **Docker** - Consistent environment

---

## 📚 Referensi

- [Heroku Documentation](https://devcenter.heroku.com/)
- [Railway Documentation](https://docs.railway.app/)
- [PythonAnywhere Documentation](https://help.pythonanywhere.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Systemd Documentation](https://systemd.io/)

---

**Selamat deploy!** 🚀
