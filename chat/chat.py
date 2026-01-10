from storage import fetch_users
from users import check_user_in_db
import uuid

def to_dict(chat, sender, receiver):

    return {
        "chat_message": chat,
        "sender": sender,
        "reciever": receiver
    }


def add_chat(sender, receiver):

    if not check_user_in_db(receiver):
        return "User not found in db"
    
    message = input("Enter your chat: ")

    chat_data = to_dict(message, sender=sender, receiver=receiver)

    chat_data.update({
        "chat_id": str(uuid.uuid4())

    })



