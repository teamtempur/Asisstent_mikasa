# ❓ Frequently Asked Questions (FAQ)

Pertanyaan yang sering ditanyakan tentang Bot Telegram Claim TukTuk.

---

## 🤖 Pertanyaan Umum

### Q: Apa itu Bot Telegram Claim TukTuk?

**A:** Bot Telegram untuk mencatat dan mengelola claim ongkos tuk-tuk dengan integrasi Google Sheets. Bot ini memudahkan pencatatan, pelacakan status claim (LUNAS/BELUM LUNAS), dan rekapan data secara otomatis.

### Q: Apakah bot ini gratis?

**A:** Ya, bot ini open source dan gratis digunakan. Anda hanya perlu membayar untuk hosting jika ingin deploy ke server (atau gunakan free tier seperti Heroku/Railway).

### Q: Apakah data saya aman?

**A:** Ya, data Anda tersimpan di Google Sheets milik Anda sendiri. Bot hanya mengakses spreadsheet yang Anda berikan izin.

---

## 📱 Pertanyaan Telegram

### Q: Bagaimana cara mendapatkan token bot?

**A:**
1. Buka Telegram, cari [@BotFather](https://t.me/BotFather)
2. Kirim `/newbot`
3. Ikuti instruksi untuk membuat bot baru
4. Simpan token yang diberikan

### Q: Bot saya tidak merespons, kenapa?

**A:** Beberapa kemungkinan:
- Token bot salah atau expired
- Bot tidak sedang berjalan
- Koneksi internet bermasalah
- Cek log error untuk detail lebih lanjut

### Q: Bagaimana cara mengubah nama bot?

**A:** Kirim `/setname` ke [@BotFather](https://t.me/BotFather), lalu pilih bot Anda dan masukkan nama baru.

### Q: Bagaimana cara mengubah foto profil bot?

**A:** Kirim `/setuserpic` ke [@BotFather](https://t.me/BotFather), lalu kirim foto yang diinginkan.

---

## 📊 Pertanyaan Google Sheets

### Q: Bagaimana cara setup Google Sheets API?

**A:** Ikuti panduan lengkap di [PANDUAN_GOOGLE_SHEETS.md](PANDUAN_GOOGLE_SHEETS.md). Ringkasnya:
1. Buat project di Google Cloud Console
2. Aktifkan Google Sheets API dan Google Drive API
3. Buat Service Account dan download credentials JSON
4. Share spreadsheet dengan email service account

### Q: Error "SpreadsheetNotFound", apa yang salah?

**A:** Beberapa kemungkinan:
- Nama spreadsheet tidak sesuai dengan config
- Spreadsheet belum di-share dengan service account
- Permission belum di-set ke "Editor"

### Q: Error "credentials.json not found", bagaimana solusinya?

**A:**
- Pastikan file `credentials.json` ada di folder yang sama dengan `bot.py`
- Pastikan nama file persis `credentials.json` (bukan `credentials (1).json`)
- Pastikan file tidak corrupt

### Q: Bagaimana cara backup data?

**A:**
1. Buka Google Sheets Anda
2. File → Download → Pilih format (Excel, CSV, dll)
3. Atau copy spreadsheet: File → Make a copy

### Q: Bisakah saya menggunakan spreadsheet yang sudah ada?

**A:** Ya, asalkan:
- Struktur kolom sesuai (No, Nama, Tanggal, Jenis, dll)
- Spreadsheet di-share dengan service account
- Nama worksheet sesuai dengan config

---

## 💻 Pertanyaan Teknis

### Q: Python versi berapa yang diperlukan?

**A:** Python 3.8 atau lebih baru. Direkomendasikan Python 3.10 atau 3.11.

### Q: Bagaimana cara update bot ke versi terbaru?

**A:**
```bash
# Backup config dan credentials
cp config.py config.py.backup
cp credentials.json credentials.json.backup

# Download versi terbaru
# Extract dan replace file

# Restore backup
cp config.py.backup config.py
cp credentials.json.backup credentials.json

# Update dependencies
pip install -r requirements.txt --upgrade
```

### Q: Bagaimana cara menjalankan bot di background?

**A:**

**Windows:**
```bash
# Gunakan run.bat
run.bat
```

**Linux/Mac:**
```bash
# Gunakan screen atau tmux
screen -S bot
python3 bot.py
# Tekan Ctrl+A, lalu D untuk detach

# Atau gunakan nohup
nohup python3 bot.py &
```

### Q: Bagaimana cara stop bot?

**A:**
- Jika di terminal: Tekan `Ctrl+C`
- Jika dengan systemd: `sudo systemctl stop tuktuk-bot`
- Jika dengan PM2: `pm2 stop tuktuk-bot`

---

## 💰 Pertanyaan Keuangan

### Q: Berapa rate konversi KHR ke USD?

**A:** Default adalah 1 USD = 4000 KHR. Anda bisa mengubahnya di `config.py`:
```python
EXCHANGE_RATE = 4000  # Ganti dengan rate yang diinginkan
```

### Q: Bisakah saya menggunakan mata uang lain?

**A:** Ya, Anda bisa modifikasi kode untuk mendukung mata uang lain. Edit file `utils.py` dan `google_sheets.py`.

### Q: Bagaimana cara menghitung total claim per bulan?

**A:** Gunakan command `/rekapan` untuk melihat ringkasan total. Untuk per bulan, Anda bisa filter di Google Sheets langsung.

---

## 🔧 Pertanyaan Fitur

### Q: Bisakah saya menambahkan fitur export ke Excel?

**A:** Ya, Anda bisa menambahkan fitur tersebut dengan mengedit `bot.py` dan menambahkan command baru. Lihat `example.py` untuk contoh penggunaan modul Google Sheets.

### Q: Bisakah bot mengirim notifikasi otomatis?

**A:** Fitur ini belum tersedia di versi saat ini, tapi bisa ditambahkan dengan mengedit `bot.py` dan menambahkan scheduler.

### Q: Bisakah saya menambahkan lebih dari satu admin?

**A:** Ya, edit `config.py`:
```python
ADMIN_IDS = [123456789, 987654321, 555666777]
```

### Q: Bagaimana cara menambahkan command baru?

**A:**
1. Edit `bot.py`
2. Buat handler function baru
3. Tambahkan ke `application.add_handler()`
4. Contoh:
```python
async def my_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!")

application.add_handler(CommandHandler('mycommand', my_command))
```

---

## 🐛 Pertanyaan Troubleshooting

### Q: Bot error "ModuleNotFoundError", apa yang salah?

**A:** Dependencies belum terinstall. Jalankan:
```bash
pip install -r requirements.txt
```

### Q: Bot error "Permission denied", bagaimana solusinya?

**A:**
- Linux/Mac: `chmod +x run.sh`
- Windows: Jalankan sebagai Administrator

### Q: Bot terus restart/sendiri, kenapa?

**A:** Beberapa kemungkinan:
- Error di kode
- Token bot invalid
- Banyak instance yang berjalan
- Cek log untuk detail error

### Q: Data tidak tersimpan ke Google Sheets, kenapa?

**A:**
- Cek koneksi internet
- Cek credentials.json valid
- Cek spreadsheet di-share dengan benar
- Cek log error

---

## 🌐 Pertanyaan Deployment

### Q: Platform hosting apa yang direkomendasikan?

**A:** Untuk pemula, direkomendasikan:
- **Heroku** - Mudah, free tier tersedia
- **Railway** - Simple, free tier tersedia
- **PythonAnywhere** - Khusus Python, free tier tersedia

### Q: Apakah bisa deploy gratis?

**A:** Ya, beberapa platform menyediakan free tier:
- Heroku (dengan batasan)
- Railway (dengan batasan)
- PythonAnywhere (dengan batasan)

### Q: Bagaimana cara deploy ke Heroku?

**A:** Lihat panduan lengkap di [DEPLOY.md](DEPLOY.md).

---

## 📝 Pertanyaan Lainnya

### Q: Bagaimana cara berkontribusi?

**A:** Lihat [CONTRIBUTING.md](CONTRIBUTING.md) untuk panduan kontribusi.

### Q: Di mana saya bisa melaporkan bug?

**A:** Buat issue di repository GitHub dengan format yang sudah disediakan.

### Q: Apakah ada grup komunitas?

**A:** Saat ini belum ada grup komunitas resmi. Anda bisa membuat issue di GitHub untuk diskusi.

### Q: Bagaimana cara request fitur baru?

**A:** Buat issue di GitHub dengan label `enhancement` dan jelaskan fitur yang diinginkan.

---

## 📞 Masih Ada Pertanyaan?

Jika pertanyaan Anda tidak terjawab di sini:

1. Cek dokumentasi lainnya:
   - [README.md](README.md)
   - [INSTALL.md](INSTALL.md)
   - [PANDUAN_GOOGLE_SHEETS.md](PANDUAN_GOOGLE_SHEETS.md)
   - [DEPLOY.md](DEPLOY.md)

2. Buat issue di repository

3. Email ke: your.email@example.com

---

**Terima kasih telah menggunakan Bot Telegram Claim TukTuk!** 🛺
