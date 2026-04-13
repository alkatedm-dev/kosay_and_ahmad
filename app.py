import telebot
from flask import Flask, request

TOKEN = '8537913433:AAHebXBap3cDIzvJEE6ZClIDL9PZ88Lzqz0'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك يا قصي! 😎\nبوتك شغال وعم يسمعك هلق.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"يا قصي، أنت قلت: {message.text}")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    # تأكدت من الرابط، هاد هو رابطك الصحيح
    bot.set_webhook(url='https://kosay-and-ahmad-1.onrender.com/' + TOKEN)
    return f"<h1 style='color: #00ffcc; text-align: center;'>تم التفعيل يا بطل! 🚀</h1>", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
