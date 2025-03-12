from flask import Flask, render_template, request, jsonify, send_from_directory
from chatbot import chatbot_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    bot_response = chatbot_response(user_input)
    return jsonify({"response": bot_response})

# Google Search Console Verification Route
@app.route("/google874f8f9f03996c33.html")
def google_verification():
    return send_from_directory("static", "google874f8f9f03996c33.html")

if __name__ == "__main__":
    app.run(debug=True)
