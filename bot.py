"""
Bot Telegram untuk Asisten Pencatatan Claim TukTuk
Integrasi dengan Google Sheets
"""

import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

from config import TELEGRAM_BOT_TOKEN, ADMIN_IDS, DEBUG
from google_sheets import get_sheets_manager

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO if not DEBUG else logging.DEBUG
)
logger = logging.getLogger(__name__)

# Initialize Google Sheets
sheets = get_sheets_manager()

# ==================== STATE CONVERSATION ====================
(INPUT_NAMA, INPUT_TANGGAL, INPUT_JENIS, INPUT_ONGKOS, 
 INPUT_KETERANGAN, INPUT_STATUS, INPUT_BUKTI) = range(7)

(UPDATE_NO, UPDATE_STATUS_BARU) = range(2)

(DELETE_NO, DELETE_CONFIRM) = range(2)

# ==================== HELPER FUNCTIONS ====================

def is_authorized(user_id: int) -> bool:
    """Cek apakah user diizinkan mengakses bot"""
    if not ADMIN_IDS:
        return True
    return user_id in ADMIN_IDS

def format_currency(khr: float, usd: float) -> str:
    """Format mata uang"""
    return f"{khr:,.0f} KHR / ${usd:,.2f}"

def format_claim_row(row: dict) -> str:
    """Format satu baris data claim untuk ditampilkan"""
    return (
        f"📋 *No {row.get('No', '-')}*\n"
        f"👤 Nama: {row.get('Nama', '-')}\n"
        f"📅 Tanggal: {row.get('Tanggal', '-')}\n"
        f"🚗 Jenis: {row.get('Jenis', '-')}\n"
        f"💰 Ongkos: {format_currency(float(row.get('Ongkos (KHR)', 0) or 0), float(row.get('Ongkos ($)', 0) or 0))}\n"
        f"📝 Keterangan: {row.get('Keterangan', '-')}"
    )

# ==================== COMMAND HANDLERS ====================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk command /start"""
    user = update.effective_user
    
    # Register user ke Google Sheets
    sheets.register_user(
        user_id=user.id,
        username=user.username or "-",
        nama=user.full_name
    )
    
    welcome_text = (
        f"👋 *Halo {user.first_name}!*\n\n"
        f"Selamat datang di *Bot Asisten Claim TukTuk* 🛺\n\n"
        f"Bot ini membantu Anda mencatat dan mengelola claim ongkos tuk-tuk.\n\n"
        f"📋 *Daftar Command:*\n"
        f"/tambah - Tambah claim baru\n"
        f"/data - Lihat semua data claim\n"
        f"/rekapan - Lihat rekapan data\n"
        f"/status - Cek status claim per orang\n"
        f"/lunas - Lihat claim yang sudah lunas\n"
        f"/belumlunas - Lihat claim yang belum lunas\n"
        f"/update - Update status claim\n"
        f"/help - Bantuan penggunaan\n\n"
        f"💡 *Tips:* Gunakan /tambah untuk mulai mencatat claim baru!"
    )
    
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk command /help"""
    help_text = (
        "📖 *Panduan Penggunaan Bot*\n\n"
        
        "*📝 Mencatat Claim Baru:*\n"
        "1. Ketik /tambah\n"
        "2. Masukkan nama\n"
        "3. Masukkan tanggal (YYYY-MM-DD)\n"
        "4. Pilih jenis (Pergi/Pulang)\n"
        "5. Masukkan ongkos dalam KHR\n"
        "6. Masukkan keterangan\n"
        "7. Pilih status (LUNAS/BELUM LUNAS)\n"
        "8. Masukkan link bukti screenshot (opsional)\n\n"
        
        "*📊 Melihat Data:*\n"
        "• /data - Semua data claim\n"
        "• /rekapan - Ringkasan total\n"
        "• /status [nama] - Status per orang\n"
        "• /lunas - Claim yang sudah lunas\n"
        "• /belumlunas - Claim yang belum lunas\n\n"
        
        "*✏️ Mengelola Data:*\n"
        "• /update - Update status claim\n\n"
        
        "*💡 Tips:*\n"
        "• Format tanggal: YYYY-MM-DD (contoh: 2026-03-21)\n"
        "• Ongkos otomatis dikonversi ke USD (1 USD = 4000 KHR)\n"
        "• Simpan bukti screenshot di Google Drive dan paste linknya"
    )
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

# ==================== TAMBAH CLAIM ====================

async def tambah_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Memulai conversation untuk tambah claim"""
    await update.message.reply_text(
        "📝 *Tambah Claim Baru*\n\n"
        "Masukkan *nama* orang yang claim:",
        parse_mode='Markdown'
    )
    return INPUT_NAMA

async def input_nama(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menerima input nama"""
    context.user_data['nama'] = update.message.text.strip()
    await update.message.reply_text(
        "📅 Masukkan *tanggal* (format: YYYY-MM-DD):\n"
        "Contoh: 2026-03-21",
        parse_mode='Markdown'
    )
    return INPUT_TANGGAL

async def input_tanggal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menerima input tanggal"""
    try:
        tanggal = update.message.text.strip()
        # Validasi format tanggal
        datetime.strptime(tanggal, '%Y-%m-%d')
        context.user_data['tanggal'] = tanggal
        
        # Buat keyboard untuk pilih jenis
        keyboard = [
            [InlineKeyboardButton("🚗 Pergi", callback_data='Pergi')],
            [InlineKeyboardButton("🏠 Pulang", callback_data='Pulang')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "🚗 Pilih *jenis* perjalanan:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        return INPUT_JENIS
    except ValueError:
        await update.message.reply_text(
            "❌ Format tanggal salah!\n"
            "Masukkan tanggal dengan format YYYY-MM-DD:\n"
            "Contoh: 2026-03-21"
        )
        return INPUT_TANGGAL

async def input_jenis_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menerima pilihan jenis dari callback"""
    query = update.callback_query
    await query.answer()
    
    context.user_data['jenis'] = query.data
    await query.edit_message_text(
        "💰 Masukkan *ongkos* dalam KHR (angka saja):\n"
        "Contoh: 6300",
        parse_mode='Markdown'
    )
    return INPUT_ONGKOS

async def input_ongkos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menerima input ongkos"""
    try:
        ongkos_khr = int(update.message.text.strip())
        ongkos_usd = ongkos_khr / 4000  # Konversi ke USD
        
        context.user_data['ongkos_khr'] = ongkos_khr
        context.user_data['ongkos_usd'] = round(ongkos_usd, 3)
        
        await update.message.reply_text(
            "📝 Masukkan *keterangan* (bisa dikosongkan):\n"
            "Contoh: Driver arrived, Paid Cash",
            parse_mode='Markdown'
        )
        return INPUT_KETERANGAN
    except ValueError:
        await update.message.reply_text(
            "❌ Masukkan angka yang valid!\n"
            "Contoh: 6300"
        )
        return INPUT_ONGKOS

async def input_keterangan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menerima input keterangan"""
    context.user_data['keterangan'] = update.message.text.strip()
    
    # Buat keyboard untuk pilih status
    keyboard = [
        [InlineKeyboardButton("✅ LUNAS", callback_data='LUNAS')],
        [InlineKeyboardButton("⏳ BELUM LUNAS", callback_data='BELUM LUNAS')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "📌 Pilih *status* claim:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
    return INPUT_STATUS

async def input_status_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menerima pilihan status dari callback"""
    query = update.callback_query
    await query.answer()
    
    context.user_data['status'] = query.data
    await query.edit_message_text(
        "📸 Masukkan *link bukti screenshot* (opsional):\n"
        "Jika tidak ada, ketik '-'",
        parse_mode='Markdown'
    )
    return INPUT_BUKTI

async def input_bukti(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menerima input bukti dan menyimpan data"""
    bukti = update.message.text.strip()
    if bukti == '-':
        bukti = ''
    
    context.user_data['bukti'] = bukti
    
    # Simpan ke Google Sheets
    user = update.effective_user
    data = {
        'nama': context.user_data['nama'],
        'tanggal': context.user_data['tanggal'],
        'jenis': context.user_data['jenis'],
        'ongkos_khr': context.user_data['ongkos_khr'],
        'ongkos_usd': context.user_data['ongkos_usd'],
        'keterangan': context.user_data['keterangan'],
        'status': context.user_data['status'],
        'bukti': bukti,
        'input_oleh': f"@{user.username}" if user.username else user.full_name
    }
    
    success = sheets.add_claim(data)
    
    if success:
        # Tampilkan ringkasan
        summary = (
            f"✅ *Claim berhasil disimpan!*\n\n"
            f"👤 Nama: {data['nama']}\n"
            f"📅 Tanggal: {data['tanggal']}\n"
            f"🚗 Jenis: {data['jenis']}\n"
            f"💰 Ongkos: {format_currency(data['ongkos_khr'], data['ongkos_usd'])}\n"
            f"📝 Keterangan: {data['keterangan']}\n"
            f"📌 Status: {data['status']}\n"
            f"📸 Bukti: {bukti if bukti else '-'}\n\n"
            f"Data sudah tersimpan di Google Sheets 📊"
        )
    else:
        summary = "❌ Gagal menyimpan claim. Silakan coba lagi."
    
    await update.message.reply_text(summary, parse_mode='Markdown')
    
    # Clear user data
    context.user_data.clear()
    
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Membatalkan conversation"""
    await update.message.reply_text(
        "❌ Proses dibatalkan.",
        parse_mode='Markdown'
    )
    context.user_data.clear()
    return ConversationHandler.END

# ==================== LIHAT DATA ====================

async def data_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menampilkan semua data claim"""
    await update.message.reply_text("⏳ Sedang mengambil data...")
    
    all_data = sheets.get_all_claims()
    
    if not all_data:
        await update.message.reply_text("📭 Belum ada data claim.")
        return
    
    # Tampilkan 10 data terakhir
    recent_data = all_data[-10:] if len(all_data) > 10 else all_data
    
    text = f"📋 *Data Claim Terakhir ({len(recent_data)} dari {len(all_data)})*\n\n"
    
    for row in recent_data:
        text += format_claim_row(row) + "\n\n"
    
    await update.message.reply_text(text, parse_mode='Markdown')

async def rekapan_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menampilkan rekapan data"""
    await update.message.reply_text("⏳ Sedang menghitung rekapan...")
    
    rekapan = sheets.get_rekapan()
    
    if not rekapan:
        await update.message.reply_text("❌ Gagal mengambil rekapan.")
        return
    
    text = (
        f"📊 *REKAPAN DATA CLAIM*\n\n"
        f"📈 *Total:*\n"
        f"   • Jumlah Claim: {rekapan['total_claims']}\n"
        f"   • Total Ongkos: {format_currency(rekapan['total_khr'], rekapan['total_usd'])}\n\n"
        f"✅ *Lunas:*\n"
        f"   • Jumlah: {rekapan['total_lunas']}\n"
        f"   • Total: {format_currency(rekapan['lunas_khr'], rekapan['lunas_usd'])}\n\n"
        f"⏳ *Belum Lunas:*\n"
        f"   • Jumlah: {rekapan['total_belum_lunas']}\n"
        f"   • Total: {format_currency(rekapan['belum_khr'], rekapan['belum_usd'])}"
    )
    
    await update.message.reply_text(text, parse_mode='Markdown')

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menampilkan status claim per orang"""
    args = context.args
    
    if args:
        # Jika ada argumen, tampilkan detail per orang
        nama = ' '.join(args)
        claims = sheets.get_claims_by_name(nama)
        
        if not claims:
            await update.message.reply_text(f"📭 Tidak ada data untuk *{nama}*.", parse_mode='Markdown')
            return
        
        lunas = [c for c in claims if c.get('Status') == 'LUNAS']
        belum = [c for c in claims if c.get('Status') == 'BELUM LUNAS']
        
        total_khr = sum([float(c.get('Ongkos (KHR)', 0) or 0) for c in claims])
        total_usd = sum([float(c.get('Ongkos ($)', 0) or 0) for c in claims])
        
        text = (
            f"👤 *Status Claim: {nama}*\n\n"
            f"📊 Total Claim: {len(claims)}\n"
            f"✅ Lunas: {len(lunas)}\n"
            f"⏳ Belum Lunas: {len(belum)}\n"
            f"💰 Total Ongkos: {format_currency(total_khr, total_usd)}\n\n"
            f"*Detail Claim:*\n"
        )
        
        for c in claims:
            status_icon = "✅" if c.get('Status') == 'LUNAS' else "⏳"
            text += f"{status_icon} {c.get('Tanggal')} - {c.get('Jenis')} - {format_currency(float(c.get('Ongkos (KHR)', 0) or 0), float(c.get('Ongkos ($)', 0) or 0))}\n"
        
        await update.message.reply_text(text, parse_mode='Markdown')
    
    else:
        # Tampilkan rekapan semua orang
        await update.message.reply_text("⏳ Sedang menghitung...")
        
        rekapan = sheets.get_rekapan_per_person()
        
        if not rekapan:
            await update.message.reply_text("📭 Belum ada data.")
            return
        
        text = "📊 *Status Claim per Orang*\n\n"
        
        for nama, data in rekapan.items():
            text += (
                f"👤 *{nama}*\n"
                f"   Total: {data['total']} | "
                f"✅ {data['lunas']} | "
                f"⏳ {data['belum_lunas']}\n"
                f"   💰 {format_currency(data['total_khr'], data['total_usd'])}\n\n"
            )
        
        await update.message.reply_text(text, parse_mode='Markdown')

async def lunas_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menampilkan claim yang sudah lunas"""
    await update.message.reply_text("⏳ Sedang mengambil data...")
    
    claims = sheets.get_claims_by_status('LUNAS')
    
    if not claims:
        await update.message.reply_text("📭 Belum ada claim yang lunas.")
        return
    
    total_khr = sum([float(c.get('Ongkos (KHR)', 0) or 0) for c in claims])
    total_usd = sum([float(c.get('Ongkos ($)', 0) or 0) for c in claims])
    
    text = f"✅ *CLAIM LUNAS* ({len(claims)} claim)\n"
    text += f"💰 Total: {format_currency(total_khr, total_usd)}\n\n"
    
    # Tampilkan 10 terakhir
    for row in claims[-10:]:
        text += format_claim_row(row) + "\n\n"
    
    await update.message.reply_text(text, parse_mode='Markdown')

async def belum_lunas_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menampilkan claim yang belum lunas"""
    await update.message.reply_text("⏳ Sedang mengambil data...")
    
    claims = sheets.get_claims_by_status('BELUM LUNAS')
    
    if not claims:
        await update.message.reply_text("✅ Semua claim sudah lunas!")
        return
    
    total_khr = sum([float(c.get('Ongkos (KHR)', 0) or 0) for c in claims])
    total_usd = sum([float(c.get('Ongkos ($)', 0) or 0) for c in claims])
    
    text = f"⏳ *BELUM LUNAS* ({len(claims)} claim)\n"
    text += f"💰 Total: {format_currency(total_khr, total_usd)}\n\n"
    
    # Tampilkan semua yang belum lunas
    for row in claims:
        text += format_claim_row(row) + "\n\n"
    
    await update.message.reply_text(text, parse_mode='Markdown')

# ==================== UPDATE STATUS ====================

async def update_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Memulai conversation untuk update status"""
    await update.message.reply_text(
        "📝 *Update Status Claim*\n\n"
        "Masukkan *nomor claim* yang ingin diupdate:",
        parse_mode='Markdown'
    )
    return UPDATE_NO

async def update_no_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menerima nomor claim"""
    try:
        no_claim = int(update.message.text.strip())
        context.user_data['update_no'] = no_claim
        
        # Buat keyboard untuk pilih status baru
        keyboard = [
            [InlineKeyboardButton("✅ LUNAS", callback_data='LUNAS')],
            [InlineKeyboardButton("⏳ BELUM LUNAS", callback_data='BELUM LUNAS')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"📌 Pilih *status baru* untuk claim No {no_claim}:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        return UPDATE_STATUS_BARU
        
    except ValueError:
        await update.message.reply_text(
            "❌ Masukkan nomor claim yang valid (angka)!"
        )
        return UPDATE_NO

async def update_status_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menerima status baru dan update"""
    query = update.callback_query
    await query.answer()
    
    no_claim = context.user_data['update_no']
    new_status = query.data
    
    success = sheets.update_claim_status(no_claim, new_status)
    
    if success:
        await query.edit_message_text(
            f"✅ Status claim No {no_claim} berhasil diupdate menjadi *{new_status}*!",
            parse_mode='Markdown'
        )
    else:
        await query.edit_message_text(
            f"❌ Gagal update status. Claim No {no_claim} tidak ditemukan."
        )
    
    context.user_data.clear()
    return ConversationHandler.END

# ==================== ERROR HANDLER ====================

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle error"""
    logger.error(f"Update {update} caused error {context.error}")
    
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "❌ Terjadi kesalahan. Silakan coba lagi."
        )

# ==================== MAIN FUNCTION ====================

def main():
    """Fungsi utama untuk menjalankan bot"""
    
    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Conversation handler untuk tambah claim
    tambah_conv = ConversationHandler(
        entry_points=[CommandHandler('tambah', tambah_command)],
        states={
            INPUT_NAMA: [MessageHandler(filters.TEXT & ~filters.COMMAND, input_nama)],
            INPUT_TANGGAL: [MessageHandler(filters.TEXT & ~filters.COMMAND, input_tanggal)],
            INPUT_JENIS: [CallbackQueryHandler(input_jenis_callback, pattern='^(Pergi|Pulang)$')],
            INPUT_ONGKOS: [MessageHandler(filters.TEXT & ~filters.COMMAND, input_ongkos)],
            INPUT_KETERANGAN: [MessageHandler(filters.TEXT & ~filters.COMMAND, input_keterangan)],
            INPUT_STATUS: [CallbackQueryHandler(input_status_callback, pattern='^(LUNAS|BELUM LUNAS)$')],
            INPUT_BUKTI: [MessageHandler(filters.TEXT & ~filters.COMMAND, input_bukti)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    # Conversation handler untuk update status
    update_conv = ConversationHandler(
        entry_points=[CommandHandler('update', update_command)],
        states={
            UPDATE_NO: [MessageHandler(filters.TEXT & ~filters.COMMAND, update_no_input)],
            UPDATE_STATUS_BARU: [CallbackQueryHandler(update_status_callback, pattern='^(LUNAS|BELUM LUNAS)$')],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    # Add handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(tambah_conv)
    application.add_handler(update_conv)
    application.add_handler(CommandHandler('data', data_command))
    application.add_handler(CommandHandler('rekapan', rekapan_command))
    application.add_handler(CommandHandler('status', status_command))
    application.add_handler(CommandHandler('lunas', lunas_command))
    application.add_handler(CommandHandler('belumlunas', belum_lunas_command))
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    # Run bot
    print("🤖 Bot sedang berjalan...")
    print("Tekan Ctrl+C untuk menghentikan.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
