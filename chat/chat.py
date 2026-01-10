
from typing import Dict
import uuid
from users import check_user_in_db
from storage import save_chat


def to_dict(chat: str, sender: str, receiver: str) -> Dict[str, str]:
    """Return a normalized chat dict ready for persistence."""
    return {"chat_message": chat, "sender": sender, "receiver": receiver}


def add_chat(sender: str, receiver: str) -> Dict[str, str]:
    """Create and persist a chat message from `sender` to `receiver`.

    Returns the saved chat dict.
    """
    if not check_user_in_db(receiver):
        raise ValueError("Receiver not found in database")

    message = input("Enter your chat: ").strip()
    if not message:
        raise ValueError("Chat message cannot be empty")

    chat_data = to_dict(message, sender=sender, receiver=receiver)
    chat_data.update({"chat_id": str(uuid.uuid4())})
    save_chat(chat_data=chat_data)
    return chat_data



