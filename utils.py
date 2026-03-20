"""
Utility functions untuk Bot Telegram Claim TukTuk
"""

from datetime import datetime
import re

def validate_date(date_string: str) -> bool:
    """
    Validasi format tanggal YYYY-MM-DD
    
    Args:
        date_string: String tanggal yang akan divalidasi
    
    Returns:
        bool: True jika valid, False jika tidak
    """
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def format_date(date_string: str) -> str:
    """
    Format tanggal dari YYYY-MM-DD ke format yang lebih readable
    
    Args:
        date_string: String tanggal YYYY-MM-DD
    
    Returns:
        str: Tanggal dalam format DD MMMM YYYY (Indonesia)
    """
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        
        # Nama bulan dalam bahasa Indonesia
        bulan_indonesia = [
            'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
            'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'
        ]
        
        return f"{date_obj.day} {bulan_indonesia[date_obj.month - 1]} {date_obj.year}"
    except ValueError:
        return date_string

def convert_khr_to_usd(khr_amount: int, rate: int = 4000) -> float:
    """
    Konversi KHR ke USD
    
    Args:
        khr_amount: Jumlah dalam KHR
        rate: Rate konversi (default: 4000)
    
    Returns:
        float: Jumlah dalam USD
    """
    return round(khr_amount / rate, 3)

def convert_usd_to_khr(usd_amount: float, rate: int = 4000) -> int:
    """
    Konversi USD ke KHR
    
    Args:
        usd_amount: Jumlah dalam USD
        rate: Rate konversi (default: 4000)
    
    Returns:
        int: Jumlah dalam KHR
    """
    return int(usd_amount * rate)

def format_number(number: float, decimals: int = 0) -> str:
    """
    Format angka dengan pemisah ribuan
    
    Args:
        number: Angka yang akan diformat
        decimals: Jumlah desimal
    
    Returns:
        str: Angka dengan pemisah ribuan
    """
    if decimals == 0:
        return f"{int(number):,}"
    else:
        return f"{number:,.{decimals}f}"

def truncate_text(text: str, max_length: int = 50) -> str:
    """
    Memotong teks jika terlalu panjang
    
    Args:
        text: Teks yang akan dipotong
        max_length: Panjang maksimum
    
    Returns:
        str: Teks yang sudah dipotong
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."

def is_valid_url(url: str) -> bool:
    """
    Validasi URL
    
    Args:
        url: URL yang akan divalidasi
    
    Returns:
        bool: True jika valid, False jika tidak
    """
    if not url or url == '-':
        return False
    
    # Regex pattern untuk URL
    pattern = re.compile(
        r'^https?://'  # http:// atau https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # atau IP
        r'(?::\d+)?'  # port opsional
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return bool(pattern.match(url))

def get_current_date() -> str:
    """
    Mendapatkan tanggal hari ini dalam format YYYY-MM-DD
    
    Returns:
        str: Tanggal hari ini
    """
    return datetime.now().strftime('%Y-%m-%d')

def get_current_datetime() -> str:
    """
    Mendapatkan tanggal dan waktu sekarang
    
    Returns:
        str: Tanggal dan waktu
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def calculate_summary(claims: list) -> dict:
    """
    Menghitung ringkasan dari list claim
    
    Args:
        claims: List dictionary berisi data claim
    
    Returns:
        dict: Dictionary berisi ringkasan
    """
    total = len(claims)
    lunas = [c for c in claims if c.get('Status') == 'LUNAS']
    belum_lunas = [c for c in claims if c.get('Status') == 'BELUM LUNAS']
    
    total_khr = sum([float(c.get('Ongkos (KHR)', 0) or 0) for c in claims])
    total_usd = sum([float(c.get('Ongkos ($)', 0) or 0) for c in claims])
    
    return {
        'total': total,
        'total_lunas': len(lunas),
        'total_belum_lunas': len(belum_lunas),
        'total_khr': total_khr,
        'total_usd': total_usd,
        'lunas_khr': sum([float(c.get('Ongkos (KHR)', 0) or 0) for c in lunas]),
        'lunas_usd': sum([float(c.get('Ongkos ($)', 0) or 0) for c in lunas]),
        'belum_khr': sum([float(c.get('Ongkos (KHR)', 0) or 0) for c in belum_lunas]),
        'belum_usd': sum([float(c.get('Ongkos ($)', 0) or 0) for c in belum_lunas])
    }

def create_progress_bar(current: int, total: int, length: int = 20) -> str:
    """
    Membuat progress bar
    
    Args:
        current: Nilai saat ini
        total: Nilai total
        length: Panjang progress bar
    
    Returns:
        str: Progress bar dalam bentuk string
    """
    if total == 0:
        return "□" * length
    
    filled = int((current / total) * length)
    return "■" * filled + "□" * (length - filled)

def escape_markdown(text: str) -> str:
    """
    Escape karakter khusus Markdown
    
    Args:
        text: Teks yang akan di-escape
    
    Returns:
        str: Teks yang sudah di-escape
    """
    if not text:
        return ""
    
    # Karakter yang perlu di-escape di Markdown
    chars_to_escape = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    
    for char in chars_to_escape:
        text = text.replace(char, f'\\{char}')
    
    return text
