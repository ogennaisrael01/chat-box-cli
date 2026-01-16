
from typing import Dict
import uuid
from users import check_user_in_db
from storage import save_chat, save_chat_ai, fetch_last_n_chats
from datetime import datetime
from gen_ai import chats_ai


def to_dict(chat: str, sender: str, receiver: str) -> Dict[str, str]:
    """Return a normalized chat dict."""
    return {"chat_message": chat, "sender": sender, "receiver": receiver}

def to_dict_ai_chat(sender: str, message:str, ai_response: str, date_created:  datetime, role: str):
    """Return a chat dict """
    return {"sender": sender, "message": message, "ai_response": ai_response, "date_created": date_created, "role": role}

def add_chat(sender: str, receiver: str) -> Dict[str, str]:
    """Create and persist a chat message from `sender` to `receiver`.

    Returns the saved chat dict.
    """
    if not check_user_in_db(receiver.title()):
        raise ValueError("Receiver not found in database")

    message = input("\n\nEnter your chat: ").strip()
    if not message:
        raise ValueError("Chat message cannot be empty")

    chat_data = to_dict(message, sender=sender, receiver=receiver)
    chat_data.update({"chat_id": str(uuid.uuid4())})
    save_chat(chat_data=chat_data)
    return chat_data

def add_chat_role_user(sender: str, message: str) -> Dict[str, str]:
    if not check_user_in_db(sender.title()):
        raise ValueError("User not found")
    if message is None:
        raise ValueError("message cannot be empty")
    chats_data = to_dict_ai_chat(sender=sender, message=message, ai_response=None, date_created=datetime.now(), role="user")
    chats_data.update({"chat_ai_id": str(uuid.uuid4())})
    save_chat_ai(chats_data)
    return chats_data

def add_chat_role_model(sender, message):
    if not check_user_in_db(sender.title()):
        raise ValueError("User not found")
    if message is None:
        raise ValueError("message cannot be empty")
    previous_chats = fetch_last_n_chats(sender=sender)
    print(previous_chats)
    gen_ai_response = chats_ai(message=message, history=previous_chats)
    chats_data = to_dict_ai_chat(sender=sender, message=message, ai_response=gen_ai_response, date_created=datetime.now(), role="model")
    chats_data.update({"chat_ai_id": str(uuid.uuid4())})
    save_chat_ai(chats_data)
    return chats_data






