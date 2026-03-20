# 🤝 Panduan Kontribusi - Bot Telegram Claim TukTuk

Terima kasih atas minat Anda untuk berkontribusi pada project ini! 🎉

---

## 📋 Cara Berkontribusi

### 1. Fork Repository

1. Buka halaman repository
2. Klik tombol **"Fork"** di pojok kanan atas
3. Pilih akun Anda untuk membuat fork

### 2. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/telegram-bot-tuktuk.git
cd telegram-bot-tuktuk
```

### 3. Buat Branch Baru

```bash
git checkout -b feature/nama-fitur-anda
# atau
git checkout -b fix/nama-bug-yang-di-fix
```

### 4. Lakukan Perubahan

- Edit file yang diperlukan
- Pastikan kode mengikuti style guide
- Tambahkan test jika diperlukan

### 5. Commit dan Push

```bash
git add .
git commit -m "Add: deskripsi fitur yang ditambahkan"
git push origin feature/nama-fitur-anda
```

### 6. Buat Pull Request

1. Buka repository asli
2. Klik **"New Pull Request"**
3. Pilih branch Anda
4. Isi deskripsi PR dengan jelas
5. Klik **"Create Pull Request"**

---

## 📝 Format Commit Message

Gunakan format berikut untuk commit message:

```
<type>: <deskripsi singkat>

<deskripsi detail (opsional)>
```

### Tipe Commit

| Tipe | Deskripsi | Contoh |
|------|-----------|--------|
| `Add` | Menambahkan fitur baru | `Add: fitur export ke Excel` |
| `Fix` | Memperbaiki bug | `Fix: error saat input tanggal` |
| `Update` | Update fitur yang ada | `Update: improve performa bot` |
| `Refactor` | Refactor kode | `Refactor: clean up code` |
| `Docs` | Update dokumentasi | `Docs: update README` |
| `Test` | Menambah/mengubah test | `Test: add unit test` |
| `Chore` | Maintenance | `Chore: update dependencies` |

---

## 🎨 Style Guide

### Python Code Style

Ikuti [PEP 8](https://pep8.org/) untuk style guide Python:

```python
# ✅ Benar
def calculate_total(claims):
    """Calculate total from list of claims."""
    return sum(claim['amount'] for claim in claims)

# ❌ Salah
def calculateTotal(Claims):
    total=0
    for i in range(len(Claims)):
        total+=Claims[i]['amount']
    return total
```

### Naming Convention

| Tipe | Convention | Contoh |
|------|------------|--------|
| Variable | snake_case | `user_name` |
| Function | snake_case | `get_data()` |
| Class | PascalCase | `GoogleSheetsManager` |
| Constant | UPPER_CASE | `MAX_RETRY` |
| Private | _leading_underscore | `_internal_var` |

### Docstring

Gunakan Google-style docstring:

```python
def function_name(param1, param2):
    """
    Deskripsi singkat fungsi.
    
    Deskripsi detail fungsi yang lebih panjang.
    
    Args:
        param1 (type): Deskripsi param1
        param2 (type): Deskripsi param2
    
    Returns:
        type: Deskripsi return value
    
    Raises:
        ExceptionType: Kapan exception terjadi
    
    Example:
        >>> function_name(1, 2)
        3
    """
    return param1 + param2
```

---

## 🧪 Testing

### Menjalankan Test

```bash
# Jalankan semua test
python test_bot.py

# Jalankan dengan verbose
python test_bot.py -v
```

### Menulis Test Baru

```python
import unittest
from utils import validate_date

class TestNewFeature(unittest.TestCase):
    
    def test_something(self):
        """Test description"""
        result = validate_date('2026-03-21')
        self.assertTrue(result)
```

---

## 📚 Dokumentasi

### Update README

Jika menambahkan fitur baru:

1. Update **Daftar Command** di README.md
2. Tambahkan contoh penggunaan
3. Update **Changelog**

### Kode Dokumentasi

Pastikan setiap fungsi/class memiliki docstring:

```python
def add_claim(data):
    """
    Menambahkan claim baru ke Google Sheets.
    
    Args:
        data (dict): Dictionary dengan keys:
            - nama (str): Nama orang
            - tanggal (str): Tanggal claim
            - jenis (str): Pergi/Pulang
            - ongkos_khr (int): Ongkos dalam KHR
            - status (str): LUNAS/BELUM LUNAS
    
    Returns:
        bool: True jika berhasil, False jika gagal
    
    Example:
        >>> data = {'nama': 'Apem', 'tanggal': '2026-03-21', ...}
        >>> add_claim(data)
        True
    """
    # Implementation
```

---

## 🐛 Melaporkan Bug

### Format Laporan Bug

Gunakan format berikut:

```markdown
**Deskripsi Bug**
Deskripsi singkat bug yang terjadi.

**Cara Reproduce**
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior**
Apa yang seharusnya terjadi.

**Actual Behavior**
Apa yang sebenarnya terjadi.

**Screenshots**
Jika ada, tambahkan screenshot.

**Environment**
- OS: [contoh: Windows 10]
- Python Version: [contoh: 3.11]
- Bot Version: [contoh: 1.0.0]

**Additional Context**
Informasi tambahan lainnya.
```

---

## 💡 Mengusulkan Fitur

### Format Request Fitur

```markdown
**Deskripsi Fitur**
Deskripsi singkat fitur yang diusulkan.

**Motivasi**
Mengapa fitur ini dibutuhkan?

**Solusi yang Diusulkan**
Bagaimana fitur ini seharusnya bekerja?

**Alternatif**
Alternatif solusi lain yang sudah dipertimbangkan.

**Additional Context**
Mockup, contoh, atau referensi lain.
```

---

## ✅ Checklist Sebelum PR

Sebelum membuat Pull Request, pastikan:

- [ ] Kode sudah di-test
- [ ] Tidak ada error
- [ ] Mengikuti style guide
- [ ] Sudah di-update dengan branch utama
- [ ] Commit message jelas
- [ ] Dokumentasi sudah di-update
- [ ] Tidak ada file yang tidak perlu

---

## 🏷️ Label

Label yang digunakan di project ini:

| Label | Deskripsi |
|-------|-----------|
| `bug` | Sesuatu tidak berfungsi |
| `enhancement` | Fitur baru |
| `documentation` | Dokumentasi |
| `good first issue` | Cocok untuk pemula |
| `help wanted` | Butuh bantuan |
| `question` | Pertanyaan |

---

## 📞 Kontak

Jika ada pertanyaan:

- Buat issue di repository
- Email: your.email@example.com

---

## 🙏 Terima Kasih

Terima kasih telah berkontribusi! Setiap kontribusi sangat berarti untuk perkembangan project ini.

**Happy Contributing!** 🎉
