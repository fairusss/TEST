from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# ====== CONFIG ======
BOT_TOKEN = os.environ.get("BOT_TOKEN") or "YOUR_BOT_TOKEN_HERE"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
WEBAPP_URL = "https://telegram-webapp-bot-ubzl.onrender.com/webapp"  # replace with your deployed URL


# ====== TELEGRAM WEBHOOK ======
@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if not data:
        return jsonify(ok=True)

    # Debug log
    print("Webhook update:", data, flush=True)

    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        # /start command sends WebApp button
        if text == "/start":
            keyboard = {
                "keyboard": [[{"text": "🌐 Open WebApp", "web_app": {"url": WEBAPP_URL}}]],
                "resize_keyboard": True,
                "one_time_keyboard": True
            }
            requests.post(f"{API_URL}/sendMessage", json={
                "chat_id": chat_id,
                "text": "Click below to open the WebApp 👇",
                "reply_markup": keyboard
            })

    return jsonify(ok=True)


# ====== SERVE WEBAPP FRONTEND ======
@app.route("/webapp")
def webapp():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Telegram WebApp</title>
        <script src="https://telegram.org/js/telegram-web-app.js"></script>
        <style>
            body { font-family: Arial; text-align: center; padding: 30px; background: #f2f2f2; }
            input { padding: 10px; width: 60%; border-radius: 8px; border: 1px solid #ccc; }
            button { padding: 10px 20px; border: none; border-radius: 8px; background: #0088cc; color: white; margin-top: 10px; cursor: pointer; }
            button:hover { background: #0077b6; }
        </style>
    </head>
    <body>
        <h2>Send a message to your bot</h2>
        <input id="userInput" placeholder="Type your message here">
        <br>
        <button id="sendBtn">Send</button>

        <script>
            const tg = window.Telegram.WebApp;
            tg.ready();
            tg.expand();

            console.log("initDataUnsafe:", tg.initDataUnsafe);

            document.getElementById("sendBtn").addEventListener("click", async () => {
                const user = tg.initDataUnsafe?.user;
                if (!user) {
                    alert("Error: Could not identify user. Open via Telegram bot button!");
                    return;
                }

                const text = document.getElementById("userInput").value;
                const payload = { user_id: user.id, text };

                const resp = await fetch("/send_message", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(payload)
                });

                const result = await resp.json();
                alert(result.status);
            });
        </script>
    </body>
    </html>
    """


# ====== RECEIVE DATA FROM WEBAPP AND SEND TO TELEGRAM ======
@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    user_id = data.get("user_id")
    text = data.get("text")

    if not user_id or not text:
        return jsonify({"status": "Error: missing user_id or text"}), 400

    resp = requests.post(f"{API_URL}/sendMessage", json={
        "chat_id": user_id,
        "text": f"💬 You sent: {text}"
    })

    return jsonify({"status": "Message sent!"})


# ====== HEALTH CHECK ======
@app.route("/")
def index():
    return "✅ Telegram WebApp Bot is running"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
