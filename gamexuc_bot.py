from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not found. Make sure it's set in your .env file.")

# English welcome message
WELCOME_TEXT_EN = """🚨 UC APOCALYPSE UNLOCKED, LEGEND! 🚨
GameXuc – Forge Your PUBG Glory! 🎮🔥💥

Yo, champ! VIP access granted for lightning-fast, secure, cheap UC drops via Chinese Method, Midasbuy, Voucher Code, iOS Login, or Huawei Login – crushing lobbies with god-tier skins & instant nukes. BOOM – delivered, no hassle!

LOCK IN: Reply “UC” + amount (60/325/1800+) + PUBG ID + method, or WhatsApp +92 335 1757574 / Telegram https://t.me/GameXUc
NEWBIE BOOST: 10% OFF FIRST HAUL!

DROP HOT & CLAIM DINNER! Your first order? 💀🏆
Your Battle Squad,
@RK_Techline
GameXuc
"""

# Russian welcome message
WELCOME_TEXT_RU = """🚨 УК АПОКАЛИПСИС РАСКРЫТ, ЛЕГЕНДА! 🚨
GameXuc – Выковывай Свою PUBG-Славу! 🎮🔥💥

Эй, чемпион! Доступ VIP открыт для молниеносных, надёжных и дешёвых поставок UC через Китайский Метод, Midasbuy, Voucher Code, iOS Login или Huawei Login – раздавливай лобби с богоподобными скинами и мгновенными нуклеарками. БУМ – доставлено, без лишней суеты!

ЗАХВАТИ ПОЗИЦИЮ: Ответь “UC” + сумма (60/325/1800+) + PUBG ID + метод, или WhatsApp +92 335 1757574 / Telegram https://t.me/GameXUc
БОНУС НОВИЧКА: 10% СКИДКИ НА ПЕРВУЮ ПОДЗАРЯДКУ!

СБРОСЬ ГОРЯЧИМ И ЗАХВАТИ УЖИН! Твой первый заказ? 💀🏆
Твой Боевой Отряд,
@RK_Techline
GameXuc
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

    await update.message.reply_text(WELCOME_TEXT_EN, reply_markup=reply_markup)
    await update.message.reply_text(WELCOME_TEXT_RU)

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
        await query.message.reply_text(WELCOME_TEXT_EN, reply_markup=reply_markup)
        await query.message.reply_text(WELCOME_TEXT_RU)

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
