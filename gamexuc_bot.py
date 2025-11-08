from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not found. Make sure it's set in your .env file.")

# Combined welcome message (English + Russian)
WELCOME_TEXT = """☠️ GameXuc Reseller Hub ☠️

Store for Resellers! 💼🎮

Dear Reseller,

Join our network for exclusive wholesale UC rates, bulk bonuses, and seamless commission payouts.
Designed to boost your PUBG sales efficiently. Enjoy secure, instant deliveries that scale with your client base.

Reply "Hi" or DM @RK_Techline to access your dealer kit and begin today.

———————————-

☠️GameXuc Reseller Hub ☠️

Магазин для реселлеров! 💼🎮
Уважаемый реселлер/дилер,

Присоединяйтесь к нашей сети для эксклюзивных оптовых тарифов UC, бонусов за опт и бесперебойных выплат комиссий 
всё разработано для эффективного роста ваших продаж PUBG. Наслаждайтесь безопасными, мгновенными доставками, которые масштабируются с вашей клиентской базой.

Ответьте «Hi» или напишите в ЛС @RK_Techline, чтобы получить дилерский набор и начать сегодня.
"""

# WhatsApp contact link
CONTACT_URL = "https://wa.me/message/M3YSQVIMPFJHM1"

# ---- Handlers ----

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("💥 Welcome", callback_data="welcome"),
            InlineKeyboardButton("📞 Contact Us", url=CONTACT_URL)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "welcome":
        keyboard = [
            [
                InlineKeyboardButton("💥 Welcome", callback_data="welcome"),
                InlineKeyboardButton("📞 Contact Us", url=CONTACT_URL)
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

# ---- Main ----
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.COMMAND, handle_message))
    app.add_handler(
        MessageHandler(filters.COMMAND, handle_message)
    )
    from telegram.ext import CallbackQueryHandler
    app.add_handler(CallbackQueryHandler(button_callback))

    print("✅ GameXUC Telegram Bot with buttons is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
