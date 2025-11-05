from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/send_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("[SERVER] Received data:", data)

    # You can do something with the data here (e.g., save to DB)
    return jsonify({"status": "success", "received": data})

if __name__ == '__main__':
    app.run(debug=True)
