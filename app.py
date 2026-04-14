import telebot
import time

TOKEN = '8537913433:AAHebXBap3cDIzvJEE6ZClIDL9PZ88Lzqz0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً يا قصي! هاد الكود الجديد شغال غصب عن الكل. كيف حالك؟")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"وصلتني رسالتك: {message.text}")

print("البوت بدأ العمل بنظام الـ Polling...")
bot.infinity_polling()
