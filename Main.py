import os
import logging
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# A simple HTML server to keep the app alive if needed
class CustomHTMLHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or not os.path.exists(self.path[1:]):
            self.path = '/index.html'
        return super().do_GET()

def run_http_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), CustomHTMLHandler)
    server.serve_forever()

# Start HTTP Server in background
threading.Thread(target=run_http_server, daemon=True).start()

# Bot Setup
BOT_TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # আপনার ছবির Direct URL (.jpg বা .png লিংক) এখানে বসাবেন
    photo_url = "https://i.ibb.co/sample-image.jpg" 

    welcome_text = (
        "🚀 <b>Welcome to Penguin Official!</b> 🐧\n\n"
        "Start earning free crypto and instant rewards by completing simple daily tasks! 💰\n\n"
        "✨ <b>Why Join Us?</b>\n"
        "🎁 <b>Signup Bonus:</b> 200 Coins\n"
        "👥 <b>Referral Reward:</b> 1,000 Coins per friend\n"
        "⚡ <b>Easy Tasks:</b> Fast & simple daily tasks\n"
        "💸 <b>Withdrawal:</b> Fast payments via USDT\n\n"
        "👇 <b>Start Earning Now:</b>"
    )

    keyboard = [
        [InlineKeyboardButton("🚀 Play App", web_app={"url": "https://penguinearnbot.blogspot.com/?m=1"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        await update.message.reply_photo(
            photo=photo_url,
            caption=welcome_text,
            parse_mode="HTML",
            reply_markup=reply_markup
        )
    except Exception:
        # ছবি লোড হতে সমস্যা হলে কেবল টেক্সট পাঠাবে
        await update.message.reply_text(
            text=welcome_text,
            parse_mode="HTML",
            reply_markup=reply_markup
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is starting...")
    app.run_polling()
