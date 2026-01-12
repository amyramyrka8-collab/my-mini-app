import telebot
import json

# --- إعدادات البوت ---
TOKEN = '8460906229:AAG2LPsjq9gdeo_HSjTbVhjoJgg1T3jZz7E'
ADMIN_ID = 5489025064 
URL = "https://amyramyrka8-collab.github.io/my-mini-app/"

# روابطك الرسمية بعد التحديث
PROOF_CHANNEL = "https://t.me/BinanceProofs_Bot"
# إذا أنشأت مجموعة نقاش ضع رابطها هنا، وإذا لم تنشئها اتركها فارغة
GROUP_LINK = "https://t.me/BinanceProofs_Bot" 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup_reply = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = telebot.types.WebAppInfo(URL)
    btn_keyboard = telebot.types.KeyboardButton("💰 فتح مركز الأرباح", web_app=web_app)
    markup_reply.add(btn_keyboard)

    markup_inline = telebot.types.InlineKeyboardMarkup()
    btn_webapp = telebot.types.InlineKeyboardButton(text="🚀 ابدأ كسب المال", web_app=web_app)
    btn_proof = telebot.types.InlineKeyboardButton(text="📸 إثباتات الدفع", url=PROOF_CHANNEL)
    
    markup_inline.add(btn_webapp)
    markup_inline.add(btn_proof)
    
    welcome_text = (f"أهلاً بك في بوت الأرباح الرسمي! ✨\n\n"
                    "يمكنك الآن جمع الدولارات من هاتفك والسحب عبر Binance Pay.\n\n"
                    "⚠️ تابع قناة الإثباتات لتتأكد من مصداقية البوت.")
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup_reply)
    bot.send_message(message.chat.id, "📢 القناة الرسمية:", reply_markup=markup_inline)

@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    try:
        data = json.loads(message.web_app_data.data)
        if data.get("type") == "withdraw":
            user_id = message.from_user.id
            amount = data.get("amount")
            wallet = data.get("wallet")

            admin_msg = (f"🚨 **طلب سحب جديد!**\n\n"
                         f"👤 المستخدم: {message.from_user.first_name}\n"
                         f"💰 المبلغ: {amount}$\n"
                         f"🟡 Binance ID: `{wallet}`")
            
            bot.send_message(ADMIN_ID, admin_msg, parse_mode="Markdown")
            bot.send_message(user_id, "✅ تم استلام طلبك! سيتم مراجعته ونشر الإثبات في قناة @BinanceProofs_Bot")

    except Exception as e:
        print(f"Error: {e}")

bot.infinity_polling()
