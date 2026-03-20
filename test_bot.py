"""
Unit Test untuk Bot Telegram Claim TukTuk
"""

import unittest
from datetime import datetime
from utils import (
    validate_date,
    format_date,
    convert_khr_to_usd,
    convert_usd_to_khr,
    format_number,
    truncate_text,
    is_valid_url,
    get_current_date,
    calculate_summary
)

class TestUtils(unittest.TestCase):
    """Test utility functions"""
    
    def test_validate_date_valid(self):
        """Test validasi tanggal yang valid"""
        self.assertTrue(validate_date('2026-03-21'))
        self.assertTrue(validate_date('2025-12-31'))
        self.assertTrue(validate_date('2024-01-01'))
    
    def test_validate_date_invalid(self):
        """Test validasi tanggal yang tidak valid"""
        self.assertFalse(validate_date('21-03-2026'))  # Format salah
        self.assertFalse(validate_date('2026/03/21'))  # Separator salah
        self.assertFalse(validate_date('invalid'))      # Bukan tanggal
        self.assertFalse(validate_date(''))             # Kosong
    
    def test_format_date(self):
        """Test format tanggal"""
        result = format_date('2026-03-21')
        self.assertIn('21', result)
        self.assertIn('2026', result)
    
    def test_convert_khr_to_usd(self):
        """Test konversi KHR ke USD"""
        self.assertEqual(convert_khr_to_usd(4000), 1.0)
        self.assertEqual(convert_khr_to_usd(8000), 2.0)
        self.assertEqual(convert_khr_to_usd(6200, 4000), 1.55)
    
    def test_convert_usd_to_khr(self):
        """Test konversi USD ke KHR"""
        self.assertEqual(convert_usd_to_khr(1.0), 4000)
        self.assertEqual(convert_usd_to_khr(2.0), 8000)
        self.assertEqual(convert_usd_to_khr(1.55), 6200)
    
    def test_format_number(self):
        """Test format angka"""
        self.assertEqual(format_number(1000), '1,000')
        self.assertEqual(format_number(1000000), '1,000,000')
        self.assertEqual(format_number(1234.56, 2), '1,234.56')
    
    def test_truncate_text(self):
        """Test truncate teks"""
        long_text = "A" * 100
        result = truncate_text(long_text, 50)
        self.assertEqual(len(result), 50)
        self.assertTrue(result.endswith('...'))
        
        short_text = "Short"
        self.assertEqual(truncate_text(short_text, 50), short_text)
    
    def test_is_valid_url(self):
        """Test validasi URL"""
        self.assertTrue(is_valid_url('https://google.com'))
        self.assertTrue(is_valid_url('http://example.com/path'))
        self.assertFalse(is_valid_url('not-a-url'))
        self.assertFalse(is_valid_url(''))
        self.assertFalse(is_valid_url('-'))
    
    def test_get_current_date(self):
        """Test mendapatkan tanggal hari ini"""
        result = get_current_date()
        self.assertEqual(len(result), 10)  # Format YYYY-MM-DD
        self.assertEqual(result.count('-'), 2)
    
    def test_calculate_summary(self):
        """Test kalkulasi summary"""
        claims = [
            {'Status': 'LUNAS', 'Ongkos (KHR)': 4000, 'Ongkos ($)': 1.0},
            {'Status': 'LUNAS', 'Ongkos (KHR)': 4000, 'Ongkos ($)': 1.0},
            {'Status': 'BELUM LUNAS', 'Ongkos (KHR)': 4000, 'Ongkos ($)': 1.0},
        ]
        
        summary = calculate_summary(claims)
        
        self.assertEqual(summary['total'], 3)
        self.assertEqual(summary['total_lunas'], 2)
        self.assertEqual(summary['total_belum_lunas'], 1)
        self.assertEqual(summary['total_khr'], 12000)
        self.assertEqual(summary['total_usd'], 3.0)


class TestConfig(unittest.TestCase):
    """Test konfigurasi"""
    
    def test_config_import(self):
        """Test import konfigurasi"""
        try:
            from config import (
                TELEGRAM_BOT_TOKEN,
                GOOGLE_SHEETS_CREDENTIALS_FILE,
                SPREADSHEET_NAME,
                EXCHANGE_RATE
            )
            self.assertIsNotNone(TELEGRAM_BOT_TOKEN)
            self.assertIsNotNone(GOOGLE_SHEETS_CREDENTIALS_FILE)
            self.assertIsNotNone(SPREADSHEET_NAME)
            self.assertGreater(EXCHANGE_RATE, 0)
        except ImportError as e:
            self.fail(f"Gagal import config: {e}")


class TestGoogleSheets(unittest.TestCase):
    """Test Google Sheets integration"""
    
    def test_sheets_manager_import(self):
        """Test import Google Sheets Manager"""
        try:
            from google_sheets import GoogleSheetsManager, get_sheets_manager
            self.assertIsNotNone(GoogleSheetsManager)
            self.assertIsNotNone(get_sheets_manager)
        except ImportError as e:
            self.fail(f"Gagal import google_sheets: {e}")


def run_tests():
    """Jalankan semua test"""
    
    print("=" * 50)
    print("MENJALANKAN UNIT TEST")
    print("=" * 50)
    
    # Buat test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Tambahkan test classes
    suite.addTests(loader.loadTestsFromTestCase(TestUtils))
    suite.addTests(loader.loadTestsFromTestCase(TestConfig))
    suite.addTests(loader.loadTestsFromTestCase(TestGoogleSheets))
    
    # Jalankan test
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 50)
    print("RINGKASAN TEST")
    print("=" * 50)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("\n✅ SEMUA TEST BERHASIL!")
    else:
        print("\n❌ ADA TEST YANG GAGAL!")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
