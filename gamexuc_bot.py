from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not found. Make sure it's set in your .env file.")

# Welcome message for everyone
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

# Huawei Login UC method message
HUAWEI_UC_TEXT = """🎮 GAMEX UC STORE 💎

💥 PUBG UC (Huawei Login Method) 💥

🚀 Available Packages:
* 1,800 UC — $18.5
* 3,850 UC — $36
* 8,100 UC — $73.5

⚙️ How It Works:
1️⃣ Choose your package
2️⃣ Share Huawei login details
3️⃣ Receive UC within minutes

⚡ Fast • Safe • Trusted • 100% Legit

#PUBG #PUBGUC #TopUp #GAMEXUC #PUBGMobile
"""

# iOS Login UC method message
IOS_UC_TEXT = """🍎 iOS Login Method | ⚡ Instant Delivery

💎 UC Packages:
* 1,800 UC —
* 3,850 UC —
* 8,100 UC —

🛡️ Why Choose Us:
✅ 100% Safe & Secure
✅ Fast & Trusted Service
✅ 24/7 Support

📩 DM to Order & Level Up Instantly!

#PUBG #PUBGMobile #UC #InstantDelivery #iOSMethod #TrustedSeller
"""

# Growth Pack message
GROWTH_PACK_TEXT = """🎯 PUBG GROWTH PACKS AVAILABLE 💎

📦 Prices: $1.5 | $3.2 | $4.5
⚙️ Method: Huawei Login (Safe & Secure)
⚡ Instant Delivery | 100% Legit | Trusted Service

#PUBG #GrowthPack #UC #TopUp #TrustedSeller
"""

# Chinese Method message
CHINA_METHOD_TEXT = """🇨🇳 Chinese Method (Via ID – No Login Needed)

⚡ Instant Delivery | Best Rates

💎 UC Price List:
60 UC — $1.0
325 UC — $4.4
660 UC — $8.3
1,800 UC — $19.9
3,850 UC — $39.3
8,100 UC — $77.9

🛡️ Why Choose Us:
✅ Safe & Secure
✅ Fast & Trusted
✅ Cheapest Rates
✅ 24/7 Support

📩 DM to Order & Level Up Instantly!

#PUBG #PUBGMobile #UC #ChineseMethod #InstantDelivery #SafeTopUp #TrustedSeller
"""

# ---- Handlers ----

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("VIA ID (web China) 🇨🇳", callback_data="china_method")
        ],
        [
            InlineKeyboardButton("VIA LOGIN (iOS) 🍎", callback_data="ios_uc")
        ],
        [
            InlineKeyboardButton("VIA LOGIN (Huawei) ‼️", callback_data="huawei_uc")
        ],
        [
            InlineKeyboardButton("GROWTH PACKS 📦", callback_data="growth_pack")
        ],
        [
            InlineKeyboardButton("WHATSAPP ❇️", url="https://wa.me/message/M3YSQVIMPFJHM1"),
            InlineKeyboardButton("TG CHANNEL ☎️", url="https://t.me/GameXUc")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton("VIA ID (web China) 🇨🇳", callback_data="china_method")
        ],
        [
            InlineKeyboardButton("VIA LOGIN (iOS) 🍎", callback_data="ios_uc")
        ],
        [
            InlineKeyboardButton("VIA LOGIN (Huawei) ‼️", callback_data="huawei_uc")
        ],
        [
            InlineKeyboardButton("GROWTH PACKS 📦", callback_data="growth_pack")
        ],
        [
            InlineKeyboardButton("WHATSAPP ❇️", url="https://wa.me/message/M3YSQVIMPFJHM1"),
            InlineKeyboardButton("TG CHANNEL ☎️", url="https://t.me/GameXUc")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if query.data == "welcome":
        await query.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)
    
    elif query.data == "huawei_uc":
        await query.message.reply_text(HUAWEI_UC_TEXT, reply_markup=reply_markup)
    
    elif query.data == "ios_uc":
        await query.message.reply_text(IOS_UC_TEXT, reply_markup=reply_markup)
    
    elif query.data == "growth_pack":
        await query.message.reply_text(GROWTH_PACK_TEXT, reply_markup=reply_markup)
    
    elif query.data == "china_method":
        await query.message.reply_text(CHINA_METHOD_TEXT, reply_markup=reply_markup)

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
