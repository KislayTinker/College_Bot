import os
import logging
from datetime import datetime

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

def log_conversation(chat_id, user_msg, bot_reply):
    # Global log (all chats in one file)
    with open("logs/conversations.csv", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f'"{timestamp}","{chat_id}","{user_msg}","{bot_reply}"\n')

    # User-specific log
    user_log_dir = f"logs/users"
    os.makedirs(user_log_dir, exist_ok=True)

    user_file = os.path.join(user_log_dir, f"{chat_id}.log")

    with open(user_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] User: {user_msg}\n[{timestamp}] Bot: {bot_reply}\n---\n")
