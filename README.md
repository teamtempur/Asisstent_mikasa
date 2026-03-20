# 🤖 Bot Telegram Claim TukTuk

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](VERSION)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg?logo=telegram)](https://core.telegram.org/bots)
[![Google Sheets](https://img.shields.io/badge/Google%20Sheets-API-green.svg?logo=google-sheets)](https://developers.google.com/sheets/api)

> Bot Telegram untuk mencatat dan mengelola claim ongkos tuk-tuk dengan integrasi Google Sheets.

![Bot Demo](https://via.placeholder.com/800x400?text=Bot+Telegram+Claim+TukTuk+Demo)

---

## ✨ Fitur

- 📝 **Pencatatan Claim** - Input data dengan conversation flow yang mudah
- 📊 **Rekapan Data** - Ringkasan total, lunas, dan belum lunas otomatis
- 👤 **Status per Orang** - Cek claim masing-masing orang
- ✏️ **Update Status** - Ubah status claim (LUNAS/BELUM LUNAS)
- 📡 **Google Sheets** - Sinkronisasi data otomatis ke spreadsheet
- 🔄 **Auto Konversi** - Konversi KHR ke USD otomatis
- 🛡️ **Aman** - Validasi input dan error handling

---

## 📋 Daftar Command

| Command | Deskripsi |
|---------|-----------|
| `/start` | Memulai bot dan melihat menu |
| `/tambah` | Menambahkan claim baru |
| `/data` | Melihat semua data claim |
| `/rekapan` | Melihat rekapan total |
| `/status [nama]` | Cek status claim per orang |
| `/lunas` | Melihat claim yang sudah lunas |
| `/belumlunas` | Melihat claim yang belum lunas |
| `/update` | Update status claim |
| `/help` | Bantuan penggunaan |
| `/cancel` | Membatalkan proses input |

---

## 🚀 Quick Start

### 1. Setup Bot Telegram (2 menit)

1. Buka Telegram, cari [@BotFather](https://t.me/BotFather)
2. Kirim `/newbot`
3. Simpan **Bot Token** yang diberikan

### 2. Setup Google Sheets (2 menit)

1. Buat spreadsheet baru di [Google Sheets](https://sheets.google.com)
2. Setup [Google Sheets API](PANDUAN_GOOGLE_SHEETS.md)
3. Download `credentials.json`

### 3. Jalankan Bot (1 menit)

```bash
# Install dependencies
pip install -r requirements.txt

# Edit config.py, masukkan token bot
# Jalankan
python bot.py
```

✅ **Selesai!** Bot sudah berjalan.

📖 [Panduan Lengkap](INSTALL.md) | 🚀 [Panduan Cepat](QUICKSTART.md)

---

## 📁 Struktur Project

```
telegram_bot_tuktuk/
├── bot.py                 # Kode utama bot
├── config.py              # Konfigurasi
├── google_sheets.py       # Integrasi Google Sheets
├── utils.py               # Utility functions
├── requirements.txt       # Dependencies
├── run.bat / run.sh       # Script runner
├── README.md              # Dokumentasi ini
├── INSTALL.md             # Panduan instalasi
├── QUICKSTART.md          # Panduan cepat
├── PANDUAN_GOOGLE_SHEETS.md  # Setup Google Sheets
├── DEPLOY.md              # Panduan deployment
└── FAQ.md                 # FAQ
```

---

## 🛠️ Teknologi

- [Python](https://www.python.org/) 3.8+
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) 20+
- [gspread](https://github.com/burnash/gspread) 5+
- [Google Sheets API](https://developers.google.com/sheets/api)

---

## 📸 Screenshot

### Menu Utama
```
👋 Halo User!

Selamat datang di Bot Asisten Claim TukTuk 🛺

📋 Daftar Command:
/tambah - Tambah claim baru
/data - Lihat semua data claim
/rekapan - Lihat rekapan data
/status - Cek status claim per orang
/lunas - Lihat claim yang sudah lunas
/belumlunas - Lihat claim yang belum lunas
/help - Bantuan penggunaan
```

### Rekapan Data
```
📊 REKAPAN DATA CLAIM

📈 Total:
   • Jumlah Claim: 25
   • Total Ongkos: 125,000 KHR / $31.25

✅ Lunas:
   • Jumlah: 20
   • Total: 100,000 KHR / $25.00

⏳ Belum Lunas:
   • Jumlah: 5
   • Total: 25,000 KHR / $6.25
```

---

## 🎯 Use Case

Bot ini cocok untuk:

- 🏢 **Perusahaan** - Mencatat claim transportasi karyawan
- 👥 **Tim/Group** - Mencatat pengeluaran bersama
- 🛺 **Driver TukTuk** - Mencatat ongkos harian
- 📊 **Accounting** - Tracking pengeluaran transportasi

---

## 🚀 Deployment

Bot dapat di-deploy ke berbagai platform:

| Platform | Free Tier | Link |
|----------|-----------|------|
| Heroku | ✅ | [Panduan](DEPLOY.md#heroku) |
| Railway | ✅ | [Panduan](DEPLOY.md#railway) |
| PythonAnywhere | ✅ | [Panduan](DEPLOY.md#pythonanywhere) |
| VPS/Dedicated | ❌ | [Panduan](DEPLOY.md#vps) |
| Docker | Varies | [Panduan](DEPLOY.md#docker) |

📖 [Panduan Deployment Lengkap](DEPLOY.md)

---

## 📝 Changelog

Lihat [CHANGELOG.md](CHANGELOG.md) untuk daftar perubahan.

---

## 🤝 Kontribusi

Kontribusi sangat diterima! Lihat [CONTRIBUTING.md](CONTRIBUTING.md) untuk panduan.

1. Fork repository
2. Buat branch baru (`git checkout -b feature/nama-fitur`)
3. Commit perubahan (`git commit -am 'Add: nama fitur'`)
4. Push ke branch (`git push origin feature/nama-fitur`)
5. Buat Pull Request

---

## 📄 Lisensi

Project ini dilisensikan di bawah [MIT License](LICENSE).

```
MIT License

Copyright (c) 2026 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Terima Kasih

Terima kasih kepada:

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) contributors
- [gspread](https://github.com/burnash/gspread) contributors
- Semua kontributor project ini

---

## 📞 Kontak

- Email: your.email@example.com
- Telegram: [@yourusername](https://t.me/yourusername)
- GitHub: [yourusername](https://github.com/yourusername)

---

**Selamat menggunakan Bot Telegram Claim TukTuk!** 🛺✨

Jika Anda menyukai project ini, berikan ⭐ di GitHub!
