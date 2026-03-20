# 🔒 Security Policy

## Supported Versions

Versi yang saat ini mendapatkan update security:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

Jika Anda menemukan kerentanan keamanan, mohon ikuti prosedur berikut:

### 1. Jangan Buka Issue Publik

Jangan membuka issue GitHub publik untuk melaporkan kerentanan keamanan. Ini bisa membahayakan pengguna lain.

### 2. Kirim Email ke Maintainer

Kirim email ke: **your.email@example.com**

Dengan subject: `[SECURITY] Deskripsi singkat kerentanan`

### 3. Sertakan Informasi Berikut

- Deskripsi kerentanan
- Langkah untuk mereproduce
- Versi yang terpengaruh
- Potensi dampak
- Saran perbaikan (jika ada)
- Informasi kontak Anda

### 4. Proses Respons

| Waktu       | Aksi                                      |
|-------------|-------------------------------------------|
| 24 jam      | Konfirmasi penerimaan laporan             |
| 72 jam      | Investigasi awal                          |
| 1 minggu    | Update status investigasi                 |
| 2-4 minggu  | Patch dan rilis (tergantung kompleksitas) |

### 5. Setelah Patch Dirilis

- Anda akan diberitahu
- Anda akan di-credit di release notes (jika diinginkan)
- CVE akan diajukan jika diperlukan

## Security Best Practices

### Untuk Pengguna

1. **Jaga Token Bot**
   - Jangan share token bot ke siapapun
   - Jangan commit token ke repository publik
   - Gunakan environment variables

2. **Jaga Credentials Google Sheets**
   - Jangan share file `credentials.json`
   - Jangan commit ke repository publik
   - Simpan di tempat yang aman

3. **Update Regularly**
   - Selalu update ke versi terbaru
   - Pantau release notes untuk security updates

4. **Gunakan Admin IDs**
   - Batasi akses bot dengan `ADMIN_IDS`
   - Jangan biarkan semua orang mengakses bot

### Untuk Developer

1. **Code Review**
   - Selalu review code sebelum merge
   - Perhatikan potensi security issues

2. **Dependencies**
   - Selalu update dependencies
   - Gunakan `pip-audit` untuk cek kerentanan

3. **Input Validation**
   - Validasi semua input dari user
   - Sanitize data sebelum disimpan

4. **Logging**
   - Jangan log sensitive information
   - Gunakan log level yang sesuai

## Security Features

Fitur keamanan yang sudah diimplementasikan:

- ✅ Input validation
- ✅ Environment variables untuk secrets
- ✅ .gitignore untuk file sensitif
- ✅ Admin ID restriction
- ✅ Error handling tanpa expose informasi sensitif

## Known Security Considerations

Hal-hal yang perlu diperhatikan:

1. **Google Sheets Access**
   - Service account memiliki akses penuh ke spreadsheet
   - Pastikan spreadsheet hanya berisi data yang diperlukan

2. **Bot Token**
   - Token bisa digunakan untuk mengontrol bot
   - Jika token bocor, revoke dan buat yang baru

3. **User Data**
   - Bot menyimpan ID Telegram dan username
   - Pastikan compliance dengan privacy regulations

## Security Tools

Tools yang direkomendasikan:

```bash
# Audit dependencies
pip install pip-audit
pip-audit

# Security linting
pip install bandit
bandit -r .

# Check for secrets
pip install detect-secrets
detect-secrets scan
```

## Contact

Untuk pertanyaan keamanan:

- Email: your.email@example.com
- Subject: `[SECURITY] Pertanyaan`

---

**Terima kasih telah membantu menjaga keamanan project ini!** 🔒
