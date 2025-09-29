from flask import Flask, request, jsonify
from services.faq_service import get_answer
from utils.logger import log_conversation
from routes.webhook import webhook_bp

# 1. Configure Flask to find and serve your frontend files
app = Flask(__name__, static_folder='frontend', static_url_path='/')

# Register webhook routes. The prefix makes the URL /webhook/webhook.
# You could remove url_prefix if you want it to be just /webhook.
app.register_blueprint(webhook_bp, url_prefix="/webhook")

@app.route("/")
def index():
    """Serves the main index.html file for the web interface."""
    return app.send_static_file('index.html')

@app.route("/api/message", methods=["POST"])
def api_message():
    data = request.get_json()
    user_msg = data.get("message")
    
    if not user_msg:
        return jsonify({"reply": "Please provide a message"}), 400
    
    chat_id = data.get("chat_id", "web_user")

    # 2. Pass the chat_id to get_answer to enable context management
    answer = get_answer(user_msg, chat_id)
    
    log_conversation(chat_id, user_msg, answer)

    return jsonify({"reply": answer})

if __name__ == "__main__":
    app.run(debug=True)