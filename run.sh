#!/bin/bash

# ==========================================
# BOT TELEGRAM CLAIM TUKTUK - RUNNER SCRIPT
# ==========================================

# Warna untuk output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}==========================================${NC}"
echo -e "${BLUE}   BOT TELEGRAM CLAIM TUKTUK${NC}"
echo -e "${BLUE}==========================================${NC}"
echo ""

# Cek apakah Python terinstall
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR] Python3 tidak ditemukan!${NC}"
    echo "Silakan install Python3 terlebih dahulu:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-venv"
    echo "  Mac: brew install python3"
    exit 1
fi

echo -e "${GREEN}[OK] Python3 terdeteksi${NC}"
echo ""

# Cek apakah virtual environment sudah ada
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}[INFO] Membuat virtual environment...${NC}"
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo -e "${RED}[ERROR] Gagal membuat virtual environment!${NC}"
        exit 1
    fi
    echo -e "${GREEN}[OK] Virtual environment berhasil dibuat${NC}"
else
    echo -e "${GREEN}[OK] Virtual environment sudah ada${NC}"
fi

# Aktifkan virtual environment
echo -e "${YELLOW}[INFO] Mengaktifkan virtual environment...${NC}"
source venv/bin/activate

# Install dependencies
echo -e "${YELLOW}[INFO] Mengecek dependencies...${NC}"
pip install -q -r requirements.txt
if [ $? -ne 0 ]; then
    echo -e "${RED}[ERROR] Gagal install dependencies!${NC}"
    exit 1
fi
echo -e "${GREEN}[OK] Dependencies sudah terinstall${NC}"

echo ""
echo -e "${BLUE}==========================================${NC}"
echo -e "${BLUE}   MENJALANKAN BOT...${NC}"
echo -e "${BLUE}==========================================${NC}"
echo ""
echo "Tekan Ctrl+C untuk menghentikan bot"
echo ""

# Jalankan bot
python bot.py

# Deactivate virtual environment saat selesai
deactivate

echo ""
echo -e "${YELLOW}Bot telah berhenti.${NC}"
