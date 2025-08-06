import requests
from flask import Flask
from threading import Thread
import time
from datetime import datetime

app = Flask(__name__)

BOT_TOKEN = "8111921192:AAGaMpBB4tFkHUeadZE5Oip2tE9Fi8D1V2I"
CHAT_ID = "5927722006"  # Aapka chat ID

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

def send_time_every_minute():
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        send_message(f"⏰ Abhi ka time hai: {now}")
        time.sleep(10)

@app.route('/')
def home():
    return "Telegram bot is running and sending time!"

def start_thread():
    thread = Thread(target=send_time_every_minute)
    thread.daemon = True
    thread.start()

start_thread()

if __name__ == "__main__":
    app.run()
