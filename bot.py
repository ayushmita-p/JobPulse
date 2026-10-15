import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


async def start(update, context):
    await update.message.reply_text("Hi! I am JobPulse. I will find fresher jobs for you.")


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()