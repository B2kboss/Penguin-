import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get('BOT_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """🐧 Welcome to PenguinEarn Official Bot!

🔥 Earn free coins daily
🏆 Boost your rank on the Waitlist
💸 Instant USDT Payouts

👇 Click below to enter the App!"""
    
    await update.message.reply_text(welcome_text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is starting...")
    app.run_polling()
