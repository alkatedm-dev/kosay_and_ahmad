import telebot
from flask import Flask, request
import os

TOKEN = '8537913433:AAHebXBap3cDIzvJEE6ZClIDL9PZ88Lzqz0'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "صباح الخير يا قصي! أخيراً اشتغلت.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "وصلت رسالتك يا بطل!")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://kosay-and-ahmad-1.onrender.com/' + TOKEN)
    return "البوت يعمل بنجاح!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    
