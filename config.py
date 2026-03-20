"""
Konfigurasi Bot Telegram dan Google Sheets
"""

import os
from dotenv import load_dotenv

# Load environment variables dari file .env (jika ada)
load_dotenv()

def get_env_or_default(key, default=None, cast_type=str):
    """
    Mendapatkan nilai dari environment variable atau default
    
    Args:
        key: Nama environment variable
        default: Nilai default jika tidak ditemukan
        cast_type: Tipe data untuk casting (str, int, bool, list)
    
    Returns:
        Nilai environment variable atau default
    """
    value = os.getenv(key, default)
    
    if value is None:
        return default
    
    if cast_type == bool:
        return value.lower() in ('true', '1', 'yes', 'on')
    elif cast_type == int:
        try:
            return int(value)
        except ValueError:
            return default
    elif cast_type == list:
        if not value:
            return []
        return [int(x.strip()) for x in value.split(',') if x.strip().isdigit()]
    
    return value

# ==================== KONFIGURASI TELEGRAM ====================
# Token dari @BotFather
# Cara mendapatkan:
# 1. Buka Telegram, cari @BotFather
# 2. Kirim /newbot
# 3. Ikuti instruksi
# 4. Copy token yang diberikan
TELEGRAM_BOT_TOKEN = get_env_or_default(
    'TELEGRAM_BOT_TOKEN', 
    'YOUR_BOT_TOKEN_HERE'  # Ganti dengan token Anda
)

# ID Telegram admin yang diizinkan mengakses bot
# Kosongkan [] untuk mengizinkan semua orang
# Contoh: [123456789, 987654321]
ADMIN_IDS = get_env_or_default('ADMIN_IDS', [], list)

# ==================== KONFIGURASI GOOGLE SHEETS ====================
# Nama file credentials Google Sheets API (JSON)
# Download dari Google Cloud Console > APIs & Services > Credentials
GOOGLE_SHEETS_CREDENTIALS_FILE = get_env_or_default(
    'GOOGLE_SHEETS_CREDENTIALS_FILE',
    'credentials.json'
)

# Nama spreadsheet Google Sheets Anda
SPREADSHEET_NAME = get_env_or_default(
    'SPREADSHEET_NAME',
    'Claim TukTuk'
)

# Nama worksheet untuk data claim
WORKSHEET_CLAIM = get_env_or_default(
    'WORKSHEET_CLAIM',
    'Data Claim'
)

# Nama worksheet untuk data user
WORKSHEET_USERS = get_env_or_default(
    'WORKSHEET_USERS',
    'Data Users'
)

# ==================== PENGATURAN LAINNYA ====================
# Format mata uang
CURRENCY_KHR = "KHR"
CURRENCY_USD = "$"

# Rate konversi KHR ke USD (default: 4000)
EXCHANGE_RATE = get_env_or_default('EXCHANGE_RATE', 4000, int)

# Debug mode - aktifkan untuk melihat log detail
DEBUG = get_env_or_default('DEBUG', False, bool)

# ==================== VALIDASI KONFIGURASI ====================
def validate_config():
    """
    Validasi konfigurasi yang diperlukan
    
    Returns:
        tuple: (is_valid, error_messages)
    """
    errors = []
    
    # Validasi Token
    if not TELEGRAM_BOT_TOKEN or TELEGRAM_BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        errors.append("❌ TELEGRAM_BOT_TOKEN belum diisi! Dapatkan token dari @BotFather")
    
    # Validasi Credentials File
    if not os.path.exists(GOOGLE_SHEETS_CREDENTIALS_FILE):
        errors.append(f"❌ File credentials tidak ditemukan: {GOOGLE_SHEETS_CREDENTIALS_FILE}")
        errors.append("   Download dari Google Cloud Console dan simpan di folder ini")
    
    # Validasi Exchange Rate
    if EXCHANGE_RATE <= 0:
        errors.append("❌ EXCHANGE_RATE harus lebih besar dari 0")
    
    return len(errors) == 0, errors

# Jalankan validasi saat import
if __name__ == "__main__":
    is_valid, errors = validate_config()
    
    if is_valid:
        print("✅ Konfigurasi valid!")
        print(f"   - Spreadsheet: {SPREADSHEET_NAME}")
        print(f"   - Exchange Rate: 1 USD = {EXCHANGE_RATE} KHR")
        print(f"   - Debug Mode: {'ON' if DEBUG else 'OFF'}")
    else:
        print("❌ Konfigurasi tidak valid:")
        for error in errors:
            print(f"   {error}")
