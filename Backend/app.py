from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/status")
def status():
    return jsonify({"mensaje": "Backend del Juego Matemático en Construcción"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)