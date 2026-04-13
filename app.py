import telebot
from flask import Flask, request

# التوكن الخاص بك
TOKEN = '8537913433:AAHebXBap3cDIzvJEE6ZClIDL9PZ88Lzqz0'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك يا قصي! 😎\nأنا بوتك الخاص، وجاهز للعمل 100%. كيف يمكنني مساعدتك اليوم؟")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"يا قصي، أنت قلت: {message.text}")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://kosay-and-ahmad-1.onrender.com/' + TOKEN)
    return "<h1 style='color: #00ffcc; text-align: center;'>تم تفعيل البوت بنجاح يا قصي! 🚀</h1>", 200

if __name__ == "__main__":
    app.run()
    
