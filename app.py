from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

# === Telegram Webhook ===
@app.route("/", methods=["POST"])
def webhook():
    update = request.get_json(force=True, silent=True)
    print(update, flush=True)

    if not update or "message" not in update:
        return jsonify({"ok": True})

    chat_id = update["message"]["chat"]["id"]
    text = update["message"].get("text", "")

    if text == "/start":
        webapp_url = "https://telegram-webapp-bot-ubzl.onrender.com/webapp"
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

    return jsonify({"ok": True})


# === WebApp UI ===
@app.route("/webapp")
def webapp():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <script src="https://telegram.org/js/telegram-web-app.js"></script>
        <title>Telegram WebApp</title>
        <style>
            body { font-family: Arial; text-align:center; padding:30px; }
            input { padding:10px; width:60%; border-radius:8px; border:1px solid #ccc; }
            button { padding:10px 20px; border:none; border-radius:8px; background:#0088cc; color:white; margin-top:10px; cursor:pointer; }
            button:hover { background:#0077b6; }
        </style>
    </head>
    <body>
        <h2>Send a Message to the Bot</h2>
        <input id="message" placeholder="Type your message...">
        <br>
        <button onclick="sendMessage()">Send</button>

        <script>
            const tg = window.Telegram.WebApp;
            tg.expand();

            function sendMessage() {
                const text = document.getElementById('message').value;
                fetch('/send_data', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        data: text,
                        chat_id: tg.initDataUnsafe?.user?.id
                    })
                });
                alert('Message sent!');
            }
        </script>
    </body>
    </html>
    """


# === Receive data from WebApp ===
@app.route("/send_data", methods=["POST"])
def send_data():
    data = request.get_json()
    print("Received from webapp:", data, flush=True)

    chat_id = data.get("chat_id")
    text = data.get("data")

    if chat_id and text:
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": f"💬 You said: {text}"
        })

    return jsonify({"ok": True})


@app.route("/")
def index():
    return "This is the Telegram bot server — running fine."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
