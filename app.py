import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# 🧠 Chatbot logic
def chatbot_reply(message):
    msg = message.lower()

    greetings = ["hi", "hello", "hey"]
    if any(word in msg for word in greetings):
        return random.choice([
            "Hey there! 😊",
            "Hello! How can I help you?",
            "Hi! Nice to talk to you 👋"
        ])

    elif "how are you" in msg:
        return random.choice([
            "I'm doing great! 😄",
            "All good here! What about you?",
            "Running perfectly as always 🤖"
        ])

    elif "name" in msg:
        return "I'm your smart chatbot 😎"

    elif "study" in msg or "learn" in msg:
        return "Focus on small steps daily. Consistency beats everything 📚"

    elif "project" in msg:
        return "Try building web apps, chatbots, or mini AI tools. Great for your resume! 🚀"

    elif "bye" in msg:
        return random.choice([
            "Goodbye! 👋",
            "See you soon!",
            "Take care 😊"
        ])

    elif "thanks" in msg or "thank you" in msg:
        return "You're welcome! 😄"

    else:
        return random.choice([
            "Hmm... interesting 🤔",
            "Can you tell me more?",
            "I'm still learning 😅",
            "That’s cool!"
        ])


# 🌐 Routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    reply = chatbot_reply(user_message)
    return jsonify({"reply": reply})


# ▶️ Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)