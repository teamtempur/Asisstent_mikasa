"""
Bot Telegram untuk Asisten Pencatatan Claim TukTuk
Integrasi dengan Google Sheets

Version: 1.0.0
Author: Your Name
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .config import (
    TELEGRAM_BOT_TOKEN,
    ADMIN_IDS,
    GOOGLE_SHEETS_CREDENTIALS_FILE,
    SPREADSHEET_NAME,
    WORKSHEET_CLAIM,
    WORKSHEET_USERS,
    EXCHANGE_RATE,
    DEBUG
)

from .google_sheets import GoogleSheetsManager, get_sheets_manager

__all__ = [
    'TELEGRAM_BOT_TOKEN',
    'ADMIN_IDS',
    'GOOGLE_SHEETS_CREDENTIALS_FILE',
    'SPREADSHEET_NAME',
    'WORKSHEET_CLAIM',
    'WORKSHEET_USERS',
    'EXCHANGE_RATE',
    'DEBUG',
    'GoogleSheetsManager',
    'get_sheets_manager',
]
