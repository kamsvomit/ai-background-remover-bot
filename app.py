import os
import threading
from flask import Flask
import telebot
from telebot import types
from gradio_client import Client, handle_file
from PIL import Image

# ==================== KONFIGURASI AMAN ====================
# Data diambil langsung dari "lemari rahasia" Koyeb (Environment Variables)
TOKEN_TELEGRAM = os.getenv("TOKEN_TELEGRAM")
URL_HF_SPACE = os.getenv("URL_HF_SPACE")

# Cek apakah token sudah diisi di settings Koyeb
if not TOKEN_TELEGRAM or not URL_HF_SPACE:
    print("❌ ERROR: Token atau URL belum diisi di Environment Variables!")
# =====================================================

bot = telebot.TeleBot(TOKEN_TELEGRAM)
client = Client(URL_HF_SPACE)
server = Flask(__name__)

@server.route("/")
def health_check():
    return "Final Boss BG Eraser is Online, Beb!", 200

def gaskeun_birefnet(message, file_id):
    try:
        status_msg = bot.reply_to(message, "⏳ Final Boss lagi kerja keras... Tunggu bentar ya!")
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        input_path = "input_temp.jpg"
        with open(input_path, 'wb') as f:
            f.write(downloaded_file)

        # Proses AI
        result_path = client.predict(image=handle_file(input_path), fn_index=0)

        # Konversi ke PNG High Quality
        final_output_path = "hasil_hd.png"
        img = Image.open(result_path).convert("RGBA")
        img.save(final_output_path, "PNG")

        with open(final_output_path, "rb") as f:
            bot.send_document(message.chat.id, f, visible_file_name="Hasil_FinalBoss.png", caption="✅ Beres! Ini versi PNG Transparan.")

        if os.path.exists(input_path): os.remove(input_path)
        if os.path.exists(final_output_path): os.remove(final_output_path)
        bot.delete_message(message.chat.id, status_msg.message_id)

    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('📸 Cara Pakai')
    btn2 = types.KeyboardButton('🛠️ Status AI')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "🔥 **Final Boss BG Eraser Ready!**\n\nKirim foto buat dapet hasil HD.", reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    teks = message.text.lower() if message.text else ""
    if "pakai" in teks:
        bot.reply_to(message, "📸 **Cara Pakai:**\nCukup kirim foto kamu ke sini. Kalau mau hasil maksimal (HD), kirim lewat menu **'File'** (dokumen).")
    elif "status" in teks:
        bot.reply_to(message, "🛠️ **Status AI:**\nOnline & Siap Tempur!")

@bot.message_handler(content_types=['photo', 'document'])
def handle_media(message):
    if message.content_type == 'photo':
        gaskeun_birefnet(message, message.photo[-1].file_id)
    elif message.content_type == 'document' and message.document.mime_type.startswith('image/'):
        gaskeun_birefnet(message, message.document.file_id)

if __name__ == "__main__":
    threading.Thread(target=lambda: bot.infinity_polling(non_stop=True)).start()
    port = int(os.environ.get("PORT", 8080))
    server.run(host='0.0.0.0', port=port)
