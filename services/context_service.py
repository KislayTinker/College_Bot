# in-memory context holder
conversation_context = {}

def set_context(chat_id, topic):
    """Saves the last topic for a user."""
    if topic and isinstance(topic, str): # Ensure topic is a valid string
        conversation_context[chat_id] = topic
        print(f"Context set for {chat_id}: {topic}") # For debugging

def get_context(chat_id):
    """Gets the last topic for a user."""
    return conversation_context.get(chat_id, None)
