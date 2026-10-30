from flask import Flask, request, jsonify
from password_generator import generate_password, password_strength

app = Flask(__name__)


@app.route("/")
def home():
    return "Password Generator API is running!"


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/generate", methods=["POST"])
def generate():

    data = request.get_json(silent=True) or {}

    try:
        length = data.get("length", 16)

        if isinstance(length, bool) or not isinstance(length, int):
            raise ValueError("Length must be an integer")

        password = generate_password(length)

        return jsonify({
            "password": password,
            "length": length,
            "strength": password_strength(length)
        })

    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
