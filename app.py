from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>البوت شغال بنجاح!</h1><p>أهلاً بك في موقع أحمد وكصي.</p>"

if __name__ == "__main__":
    app.run()
