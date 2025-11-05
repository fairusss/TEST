from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")  # safer than hardcoding
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    if not update:
        return jsonify({"status": "no update"})

    message = update.get("message")
    if not message:
        return jsonify({"status": "no message"})

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if text == "/start":
        webapp_url = "https://your-app-name.onrender.com"  # change after deployment
        keyboard = {
            "keyboard": [[{
                "text": "🌐 Open WebApp",
                "web_app": {"url": webapp_url}
            }]],
            "resize_keyboard": True
        }

        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": "Tap below to open the WebApp 👇",
            "reply_markup": keyboard
        })

    return jsonify({"status": "ok"})

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message', '')
    chat_id = data.get('chat_id')

    if not chat_id:
        return jsonify({"error": "Missing chat_id"}), 400

    requests.post(f"{TELEGRAM_API}/sendMessage", json={
        "chat_id": chat_id,
        "text": f"You said: {message}"
    })

    return jsonify({"status": "sent"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
