import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# السيرفر سيبحث عن التوكن تلقائياً من إعدادات البيئة
TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'مرحباً بك! أنا بوت الاقتباسات. 🪄\n'
        'أرسل الأمر /quote لأحضر لك حكمة جميلة اليوم.'
    )

async def get_quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("جاري البحث عن اقتباس... ⏳")
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()[0]
        quote_text = data['q']
        author = data['a']
        await update.message.reply_text(f'💡 "{quote_text}"\n\n— {author}')
    except Exception as e:
        await update.message.reply_text("عذراً، حدث خطأ أثناء جلب الاقتباس.")

if _name_ == '_main_':
    print("البوت يعمل الآن...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", get_quote))
    app.run_polling()