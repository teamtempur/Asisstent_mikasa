# 📋 Changelog - Bot Telegram Claim TukTuk

Semua perubahan pada project ini akan didokumentasikan di file ini.

Format berdasarkan [Keep a Changelog](https://keepachangelog.com/)
dan project ini mengikuti [Semantic Versioning](https://semver.org/).

---

## [1.0.0] - 2026-03-21

### 🎉 Rilis Pertama

Fitur-fitur yang tersedia di versi ini:

### ✨ Fitur Utama

- **📝 Pencatatan Claim**
  - Tambah claim baru dengan conversation flow
  - Input nama, tanggal, jenis (Pergi/Pulang)
  - Input ongkos dalam KHR (auto konversi ke USD)
  - Input keterangan dan link bukti screenshot
  - Pilih status (LUNAS/BELUM LUNAS)

- **📊 Rekapan Data**
  - Lihat semua data claim
  - Rekapan total (jumlah, total ongkos)
  - Rekapan per status (LUNAS/BELUM LUNAS)
  - Rekapan per orang

- **🔍 Filter dan Pencarian**
  - Filter claim berdasarkan status
  - Cek status claim per orang
  - Lihat detail claim

- **✏️ Manajemen Data**
  - Update status claim (LUNAS/BELUM LUNAS)
  - Data tersimpan di Google Sheets

### 🔧 Integrasi

- **Google Sheets API**
  - Sinkronisasi otomatis ke Google Sheets
  - Worksheet terpisah untuk data claim dan users
  - Auto-create worksheet jika belum ada

- **Telegram Bot API**
  - Menggunakan python-telegram-bot v20+
  - Conversation handler untuk input data
  - Inline keyboard untuk pilihan
  - Error handling

### 📁 Struktur File

```
telegram_bot_tuktuk/
├── bot.py                      # Kode utama bot
├── config.py                   # Konfigurasi (dengan .env support)
├── google_sheets.py            # Modul integrasi Google Sheets
├── utils.py                    # Utility functions
├── requirements.txt            # Dependencies
├── setup.py                    # Setup script
├── .env.example                # Contoh file environment
├── .gitignore                  # Git ignore rules
├── run.bat / run.sh            # Script runner dengan venv
├── start.bat / start.sh        # Script runner sederhana
├── README.md                   # Dokumentasi utama
├── INSTALL.md                  # Panduan instalasi
├── PANDUAN_GOOGLE_SHEETS.md    # Panduan setup Google Sheets
└── CHANGELOG.md                # Log perubahan (ini)
```

### 🛠️ Teknologi

- Python 3.8+
- python-telegram-bot 20+
- gspread 5+
- Google API Client
- python-dotenv

---

## [Unreleased]

### 🚧 Fitur yang Direncanakan

- [ ] Export data ke Excel/CSV
- [ ] Notifikasi otomatis untuk claim belum lunas
- [ ] Statistik grafik (chart)
- [ ] Multi-language support
- [ ] Backup dan restore data
- [ ] Web dashboard
- [ ] API endpoint

---

## Catatan Versi

### Versioning

- **MAJOR**: Perubahan besar yang tidak kompatibel dengan versi sebelumnya
- **MINOR**: Penambahan fitur baru yang kompatibel
- **PATCH**: Bug fix dan perbaikan kecil

### Format Changelog

- `Added` - Fitur baru
- `Changed` - Perubahan pada fitur yang ada
- `Deprecated` - Fitur yang akan dihapus
- `Removed` - Fitur yang dihapus
- `Fixed` - Bug fix
- `Security` - Perbaikan keamanan

---

## Kontribusi

Jika Anda ingin berkontribusi:

1. Fork repository
2. Buat branch baru (`git checkout -b feature/nama-fitur`)
3. Commit perubahan (`git commit -am 'Add: nama fitur'`)
4. Push ke branch (`git push origin feature/nama-fitur`)
5. Buat Pull Request

---

**Terima kasih telah menggunakan Bot Telegram Claim TukTuk!** 🛺
