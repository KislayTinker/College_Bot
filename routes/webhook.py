from flask import Blueprint, request, jsonify
from services.faq_service import get_answer
from services.telegram_service import send_message
from utils.logger import log_conversation
from services.nlp_service import translate_text, translate_to_original_lang

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        user_msg = data["message"]["text"]

        # Get bot reply and log conversation
        answer = get_answer(user_msg)

        # Send reply to telegram
        send_message(chat_id, answer)

        # log conversation (both global and user-specific)
        log_conversation(chat_id, user_msg, answer)

    return jsonify({"status": "ok"})
