TOKEN = "9089908731:AAGHFcKEnlWyCItZev0o5_kpdIRYPFTHS3Q"

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests, socket

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⭐ Helxt Bot online! Fai /help")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/tinfo @canale - info canale\n/ip 8.8.8.8 - info ip\n/username helxt - check username")

async def tinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args: return await update.message.reply_text("Usa: /tinfo @canale")
    try:
        chat = await context.bot.get_chat(context.args[0])
        await update.message.reply_text(f"{chat.title}\nID: {chat.id}")
    except Exception as e:
        await update.message.reply_text(str(e))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(CommandHandler("tinfo", tinfo))

print("Bot partito...")
app.run_polling()