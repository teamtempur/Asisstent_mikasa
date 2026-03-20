@echo off
chcp 65001 >nul
title Bot Telegram Claim TukTuk

echo ==========================================
echo   BOT TELEGRAM CLAIM TUKTUK
echo ==========================================
echo.

:: Cek apakah Python terinstall
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python tidak ditemukan!
    echo Silakan install Python terlebih dahulu dari https://python.org
    pause
    exit /b 1
)

echo [OK] Python terdeteksi
echo.

:: Cek apakah virtual environment sudah ada
if not exist "venv" (
    echo [INFO] Membuat virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Gagal membuat virtual environment!
        pause
        exit /b 1
    )
    echo [OK] Virtual environment berhasil dibuat
) else (
    echo [OK] Virtual environment sudah ada
)

:: Aktifkan virtual environment
echo [INFO] Mengaktifkan virtual environment...
call venv\Scripts\activate

:: Install dependencies
echo [INFO] Mengecek dependencies...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Gagal install dependencies!
    pause
    exit /b 1
)
echo [OK] Dependencies sudah terinstall

echo.
echo ==========================================
echo   MENJALANKAN BOT...
echo ==========================================
echo.
echo Tekan Ctrl+C untuk menghentikan bot
echo.

:: Jalankan bot
python bot.py

:: Deactivate virtual environment saat selesai
call venv\Scripts\deactivate

echo.
echo Bot telah berhenti.
pause
