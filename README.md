Welcome to ai background remover bot
Repo ini berisi source code untuk Bot Telegram yang berfungsi menghapus latar belakang foto secara otomatis dengan kualitas HD. Bot ini dirancang untuk mempermudah alur kerja editing foto melalui integrasi AI yang ringan dan cepat.
🔥 Fitur Utama
High-Quality BG Removal: Menghapus background foto secara instan hanya dengan mengirimkan gambar ke bot Telegram.
HD Document Output: Hasil akhir dikirim dalam format dokumen (.png transparan) agar kualitas gambar tetap terjaga dan tidak pecah saat digunakan untuk kebutuhan desain.
24/7 Standby: Menggunakan server Koyeb agar bot tetap aktif setiap saat tanpa perlu menjalankan script secara manual di komputer lokal.
🛠️ Tech Stack
Proyek ini dikembangkan menggunakan Python dengan pendekatan yang sederhana namun efektif [cite: 2026-01-25]:
Python (pyTelegramBotAPI): Digunakan sebagai library utama untuk mengelola interaksi bot [cite: 2026-01-29].
Gradio Client: Digunakan untuk menghubungkan bot dengan engine AI yang ada di Hugging Face.
Flask & Threading: Digunakan untuk menjaga bot agar tetap responsif dan memenuhi syarat health check pada layanan cloud.
Koyeb: Platform yang digunakan untuk proses deployment agar bot dapat berjalan secara stabil di awan.
📖 Cara Penggunaan
Aktifkan Bot: Jalankan perintah /start pada chat bot.
Kirim Foto: Unggah foto yang ingin dihapus latarnya (disarankan melalui fitur "File/Document" untuk hasil maksimal).
Terima Hasil: Tunggu beberapa saat hingga bot mengirimkan kembali file PNG transparan siap pakai.
🏗️ Cara Deploy
Siapkan TOKEN_TELEGRAM yang didapatkan dari BotFather.
Siapkan URL_HF_SPACE yang merujuk pada Hugging Face Space yang ingin digunakan.
Masukkan kedua variabel tersebut ke dalam bagian Environment Variables pada dashboard layanan hosting (seperti Koyeb atau Render).
"Solusi cerdas untuk urusan hapus background, bikin alur kerja jadi makin efisien."
