"""
Contoh penggunaan modul Google Sheets
File ini menunjukkan cara menggunakan GoogleSheetsManager
"""

from google_sheets import get_sheets_manager
from datetime import datetime

# Inisialisasi Google Sheets Manager
sheets = get_sheets_manager()

def example_add_claim():
    """Contoh menambahkan claim baru"""
    
    data = {
        'nama': 'Apem',
        'tanggal': '2026-03-21',
        'jenis': 'Pergi',
        'ongkos_khr': 6200,
        'ongkos_usd': 1.55,
        'keterangan': 'Driver arrived, Paid Cash',
        'status': 'LUNAS',
        'bukti': 'https://prnt.sc/abc123',
        'input_oleh': '@username'
    }
    
    success = sheets.add_claim(data)
    
    if success:
        print("✅ Claim berhasil ditambahkan!")
    else:
        print("❌ Gagal menambahkan claim")

def example_get_all_claims():
    """Contoh mengambil semua data claim"""
    
    claims = sheets.get_all_claims()
    
    print(f"📋 Total claim: {len(claims)}")
    
    for claim in claims[:5]:  # Tampilkan 5 data pertama
        print(f"  - {claim.get('Nama')} | {claim.get('Tanggal')} | {claim.get('Status')}")

def example_get_claims_by_name():
    """Contoh mengambil data berdasarkan nama"""
    
    nama = "Apem"
    claims = sheets.get_claims_by_name(nama)
    
    print(f"👤 Claim untuk {nama}: {len(claims)}")
    
    for claim in claims:
        print(f"  - {claim.get('Tanggal')} | {claim.get('Jenis')} | {claim.get('Status')}")

def example_get_claims_by_status():
    """Contoh mengambil data berdasarkan status"""
    
    # Claim yang sudah lunas
    lunas = sheets.get_claims_by_status('LUNAS')
    print(f"✅ Lunas: {len(lunas)} claim")
    
    # Claim yang belum lunas
    belum = sheets.get_claims_by_status('BELUM LUNAS')
    print(f"⏳ Belum Lunas: {len(belum)} claim")

def example_get_rekapan():
    """Contoh mendapatkan rekapan data"""
    
    rekapan = sheets.get_rekapan()
    
    print("📊 REKAPAN:")
    print(f"  Total Claims: {rekapan.get('total_claims')}")
    print(f"  Lunas: {rekapan.get('total_lunas')}")
    print(f"  Belum Lunas: {rekapan.get('total_belum_lunas')}")
    print(f"  Total Ongkos (KHR): {rekapan.get('total_khr'):,.0f}")
    print(f"  Total Ongkos ($): {rekapan.get('total_usd'):,.2f}")

def example_get_rekapan_per_person():
    """Contoh mendapatkan rekapan per orang"""
    
    rekapan = sheets.get_rekapan_per_person()
    
    print("👤 REKAPAN PER ORANG:")
    
    for nama, data in rekapan.items():
        print(f"\n  {nama}:")
        print(f"    Total: {data['total']}")
        print(f"    Lunas: {data['lunas']}")
        print(f"    Belum Lunas: {data['belum_lunas']}")
        print(f"    Total Ongkos: {data['total_khr']:,.0f} KHR / ${data['total_usd']:,.2f}")

def example_update_status():
    """Contoh update status claim"""
    
    no_claim = 1
    new_status = 'LUNAS'
    
    success = sheets.update_claim_status(no_claim, new_status)
    
    if success:
        print(f"✅ Status claim No {no_claim} diupdate menjadi {new_status}")
    else:
        print(f"❌ Gagal update status claim No {no_claim}")

def example_register_user():
    """Contoh mendaftarkan user"""
    
    user_id = 123456789
    username = "@testuser"
    nama = "Test User"
    
    success = sheets.register_user(user_id, username, nama)
    
    if success:
        print(f"✅ User {username} berhasil terdaftar")
    else:
        print(f"❌ Gagal mendaftarkan user")

def example_get_all_users():
    """Contoh mengambil semua data user"""
    
    users = sheets.get_all_users()
    
    print(f"👥 Total users: {len(users)}")
    
    for user in users:
        print(f"  - {user.get('Username')} | {user.get('Nama')}")

# ==================== MAIN ====================

if __name__ == "__main__":
    
    print("=" * 50)
    print("CONTOH PENGGUNAAN GOOGLE SHEETS MANAGER")
    print("=" * 50)
    
    # Pilih contoh yang ingin dijalankan
    
    # example_add_claim()
    # example_get_all_claims()
    # example_get_claims_by_name()
    # example_get_claims_by_status()
    # example_get_rekapan()
    # example_get_rekapan_per_person()
    # example_update_status()
    # example_register_user()
    # example_get_all_users()
    
    # Jalankan semua contoh
    print("\n1. Menambahkan claim baru...")
    example_add_claim()
    
    print("\n2. Mengambil semua claim...")
    example_get_all_claims()
    
    print("\n3. Mengambil claim berdasarkan nama...")
    example_get_claims_by_name()
    
    print("\n4. Mengambil claim berdasarkan status...")
    example_get_claims_by_status()
    
    print("\n5. Mendapatkan rekapan...")
    example_get_rekapan()
    
    print("\n6. Mendapatkan rekapan per orang...")
    example_get_rekapan_per_person()
    
    print("\n7. Mendaftarkan user...")
    example_register_user()
    
    print("\n8. Mengambil semua users...")
    example_get_all_users()
    
    print("\n" + "=" * 50)
    print("SELESAI!")
    print("=" * 50)
