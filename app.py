from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ESTA FUNÇÃO DEVE ATENDER APENAS A ROTA "/"
@app.route("/")
def home_page():
    return render_template("index.html")

# ESTA FUNÇÃO DEVE ATENDER APENAS A ROTA "/api/status"
@app.route("/api/status")
def api_status():
    return jsonify({
        "status": "ok",
        "message": "Seu app Flask está vivo!"
    })

if __name__ == "__main__":
    app.run(debug=True)



