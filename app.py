import telebot
from flask import Flask, request
import os

TOKEN = '8537913433:AAHebXBap3cDIzvJEE6ZClIDL9PZ88Lzqz0'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    # تأكد إن الرابط هون فيه التوكن في آخره
    bot.set_webhook(url='https://kosay-and-ahmad-1.onrender.com/' + TOKEN)
    return "OK", 200

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "أخيراً يا قصي! أنا شغال وعم بسمعك.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
