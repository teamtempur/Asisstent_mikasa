"""
Modul Integrasi Google Sheets
Menangani koneksi dan operasi CRUD ke Google Sheets
"""

import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime
import json
import os
from config import (
    GOOGLE_SHEETS_CREDENTIALS_FILE, 
    SPREADSHEET_NAME, 
    WORKSHEET_CLAIM, 
    WORKSHEET_USERS,
    DEBUG
)

class GoogleSheetsManager:
    """Kelas untuk mengelola koneksi dan operasi Google Sheets"""
    
    def __init__(self):
        self.client = None
        self.spreadsheet = None
        self.claim_sheet = None
        self.users_sheet = None
        self._connect()
    
    def _connect(self):
        """Membuat koneksi ke Google Sheets API"""
        try:
            # Scope yang diperlukan untuk Google Sheets
            scope = [
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive',
                'https://www.googleapis.com/auth/spreadsheets'
            ]
            
            # Load credentials dari file JSON
            if os.path.exists(GOOGLE_SHEETS_CREDENTIALS_FILE):
                creds = Credentials.from_service_account_file(
                    GOOGLE_SHEETS_CREDENTIALS_FILE, 
                    scopes=scope
                )
                self.client = gspread.authorize(creds)
                
                # Buka spreadsheet
                self.spreadsheet = self.client.open(SPREADSHEET_NAME)
                
                # Buka worksheet
                try:
                    self.claim_sheet = self.spreadsheet.worksheet(WORKSHEET_CLAIM)
                except gspread.WorksheetNotFound:
                    self.claim_sheet = self.spreadsheet.add_worksheet(
                        title=WORKSHEET_CLAIM, 
                        rows=1000, 
                        cols=15
                    )
                    self._init_claim_sheet()
                
                try:
                    self.users_sheet = self.spreadsheet.worksheet(WORKSHEET_USERS)
                except gspread.WorksheetNotFound:
                    self.users_sheet = self.spreadsheet.add_worksheet(
                        title=WORKSHEET_USERS, 
                        rows=100, 
                        cols=5
                    )
                    self._init_users_sheet()
                
                if DEBUG:
                    print("✅ Berhasil terhubung ke Google Sheets")
            else:
                print(f"❌ File credentials tidak ditemukan: {GOOGLE_SHEETS_CREDENTIALS_FILE}")
                
        except Exception as e:
            print(f"❌ Error koneksi Google Sheets: {str(e)}")
            raise
    
    def _init_claim_sheet(self):
        """Inisialisasi header untuk worksheet claim"""
        headers = [
            "No", "Nama", "Tanggal", "Jenis", "Ongkos (KHR)", 
            "Ongkos ($)", "Keterangan", "Status", "Bukti Screenshot",
            "Input Oleh", "Waktu Input"
        ]
        self.claim_sheet.append_row(headers)
    
    def _init_users_sheet(self):
        """Inisialisasi header untuk worksheet users"""
        headers = ["ID Telegram", "Username", "Nama", "Waktu Registrasi"]
        self.users_sheet.append_row(headers)
    
    # ==================== OPERASI DATA CLAIM ====================
    
    def add_claim(self, data):
        """
        Menambahkan claim baru ke Google Sheets
        
        Args:
            data: Dictionary dengan keys: nama, tanggal, jenis, ongkos_khr, 
                  ongkos_usd, keterangan, status, bukti, input_oleh
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        try:
            # Dapatkan nomor urut terakhir
            all_data = self.claim_sheet.get_all_values()
            last_no = len(all_data) if len(all_data) > 1 else 1
            
            row_data = [
                last_no,  # No
                data.get('nama', ''),
                data.get('tanggal', datetime.now().strftime('%Y-%m-%d')),
                data.get('jenis', ''),
                data.get('ongkos_khr', 0),
                data.get('ongkos_usd', 0),
                data.get('keterangan', ''),
                data.get('status', 'BELUM LUNAS'),
                data.get('bukti', ''),
                data.get('input_oleh', ''),
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ]
            
            self.claim_sheet.append_row(row_data)
            return True
            
        except Exception as e:
            print(f"❌ Error menambahkan claim: {str(e)}")
            return False
    
    def get_all_claims(self):
        """
        Mengambil semua data claim
        
        Returns:
            list: List of dictionaries berisi data claim
        """
        try:
            all_data = self.claim_sheet.get_all_records()
            return all_data
        except Exception as e:
            print(f"❌ Error mengambil data: {str(e)}")
            return []
    
    def get_claims_by_name(self, nama):
        """
        Mengambil data claim berdasarkan nama
        
        Args:
            nama: Nama orang yang claim
        
        Returns:
            list: List of dictionaries berisi data claim
        """
        try:
            all_data = self.get_all_claims()
            filtered = [row for row in all_data if row.get('Nama', '').lower() == nama.lower()]
            return filtered
        except Exception as e:
            print(f"❌ Error mengambil data: {str(e)}")
            return []
    
    def get_claims_by_status(self, status):
        """
        Mengambil data claim berdasarkan status
        
        Args:
            status: 'LUNAS' atau 'BELUM LUNAS'
        
        Returns:
            list: List of dictionaries berisi data claim
        """
        try:
            all_data = self.get_all_claims()
            filtered = [row for row in all_data if row.get('Status', '') == status]
            return filtered
        except Exception as e:
            print(f"❌ Error mengambil data: {str(e)}")
            return []
    
    def update_claim_status(self, no_claim, new_status):
        """
        Update status claim
        
        Args:
            no_claim: Nomor claim
            new_status: Status baru ('LUNAS' atau 'BELUM LUNAS')
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        try:
            # Cari baris dengan nomor claim
            all_data = self.claim_sheet.get_all_values()
            for i, row in enumerate(all_data):
                if i > 0 and str(row[0]) == str(no_claim):
                    # Update kolom status (kolom ke-8, index 7)
                    self.claim_sheet.update_cell(i + 1, 8, new_status)
                    return True
            return False
        except Exception as e:
            print(f"❌ Error update status: {str(e)}")
            return False
    
    # ==================== REKAPAN DATA ====================
    
    def get_rekapan(self):
        """
        Mendapatkan rekapan data claim
        
        Returns:
            dict: Dictionary berisi rekapan
        """
        try:
            all_data = self.get_all_claims()
            
            total_claims = len(all_data)
            lunas = [row for row in all_data if row.get('Status', '') == 'LUNAS']
            belum_lunas = [row for row in all_data if row.get('Status', '') == 'BELUM LUNAS']
            
            # Hitung total ongkos
            total_khr = sum([float(row.get('Ongkos (KHR)', 0) or 0) for row in all_data])
            total_usd = sum([float(row.get('Ongkos ($)', 0) or 0) for row in all_data])
            
            lunas_khr = sum([float(row.get('Ongkos (KHR)', 0) or 0) for row in lunas])
            lunas_usd = sum([float(row.get('Ongkos ($)', 0) or 0) for row in lunas])
            
            belum_khr = sum([float(row.get('Ongkos (KHR)', 0) or 0) for row in belum_lunas])
            belum_usd = sum([float(row.get('Ongkos ($)', 0) or 0) for row in belum_lunas])
            
            return {
                'total_claims': total_claims,
                'total_lunas': len(lunas),
                'total_belum_lunas': len(belum_lunas),
                'total_khr': total_khr,
                'total_usd': total_usd,
                'lunas_khr': lunas_khr,
                'lunas_usd': lunas_usd,
                'belum_khr': belum_khr,
                'belum_usd': belum_usd
            }
            
        except Exception as e:
            print(f"❌ Error menghitung rekapan: {str(e)}")
            return {}
    
    def get_rekapan_per_person(self):
        """
        Mendapatkan rekapan data per orang
        
        Returns:
            dict: Dictionary berisi rekapan per orang
        """
        try:
            all_data = self.get_all_claims()
            
            rekapan = {}
            for row in all_data:
                nama = row.get('Nama', '')
                if not nama:
                    continue
                
                if nama not in rekapan:
                    rekapan[nama] = {
                        'total': 0,
                        'lunas': 0,
                        'belum_lunas': 0,
                        'total_khr': 0,
                        'total_usd': 0,
                        'lunas_khr': 0,
                        'lunas_usd': 0,
                        'belum_khr': 0,
                        'belum_usd': 0
                    }
                
                ongkos_khr = float(row.get('Ongkos (KHR)', 0) or 0)
                ongkos_usd = float(row.get('Ongkos ($)', 0) or 0)
                status = row.get('Status', '')
                
                rekapan[nama]['total'] += 1
                rekapan[nama]['total_khr'] += ongkos_khr
                rekapan[nama]['total_usd'] += ongkos_usd
                
                if status == 'LUNAS':
                    rekapan[nama]['lunas'] += 1
                    rekapan[nama]['lunas_khr'] += ongkos_khr
                    rekapan[nama]['lunas_usd'] += ongkos_usd
                else:
                    rekapan[nama]['belum_lunas'] += 1
                    rekapan[nama]['belum_khr'] += ongkos_khr
                    rekapan[nama]['belum_usd'] += ongkos_usd
            
            return rekapan
            
        except Exception as e:
            print(f"❌ Error menghitung rekapan per orang: {str(e)}")
            return {}
    
    # ==================== OPERASI DATA USER ====================
    
    def register_user(self, user_id, username, nama):
        """
        Mendaftarkan user baru
        
        Args:
            user_id: ID Telegram user
            username: Username Telegram
            nama: Nama lengkap
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        try:
            # Cek apakah user sudah terdaftar
            all_users = self.users_sheet.get_all_values()
            for row in all_users:
                if str(row[0]) == str(user_id):
                    return True  # User sudah terdaftar
            
            row_data = [
                user_id,
                username,
                nama,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ]
            
            self.users_sheet.append_row(row_data)
            return True
            
        except Exception as e:
            print(f"❌ Error mendaftarkan user: {str(e)}")
            return False
    
    def get_all_users(self):
        """
        Mengambil semua data user
        
        Returns:
            list: List of dictionaries berisi data user
        """
        try:
            all_data = self.users_sheet.get_all_records()
            return all_data
        except Exception as e:
            print(f"❌ Error mengambil data user: {str(e)}")
            return []


# Singleton instance
_sheets_manager = None

def get_sheets_manager():
    """Mendapatkan instance GoogleSheetsManager (singleton)"""
    global _sheets_manager
    if _sheets_manager is None:
        _sheets_manager = GoogleSheetsManager()
    return _sheets_manager
