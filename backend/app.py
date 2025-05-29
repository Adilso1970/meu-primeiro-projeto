import os
from flask import Flask, jsonify

app = Flask(__name__)

# === Health Check ===
@app.route("/health")
def health():
    return jsonify({"status": "ok"})

# === Seus endpoints de verdade ===
@app.route("/api/message")
def message():
    return jsonify({"msg": "Olá do Flask!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

