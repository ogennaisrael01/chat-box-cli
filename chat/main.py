import argparse
import logging
from users import add_account, check_user_in_db
from storage import create_table_users, create_chat_table, fetch_chats, create_chat_ai_table
from chats import add_chat, add_chat_role_user, add_chat_role_model
import time


logger = logging.getLogger(__name__)
def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="chat_box")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("init-db", help="Create the database tables")
    sub.add_parser("add-user", help="Interactively add a user")
    sub.add_parser("add-chat", help="Interactively chat with a user")
    sub.add_parser("chat-ai", help="Interactively chat with ai")

    args = parser.parse_args(argv)

    if args.command == "init-db":
        try:
            create_table_users()
            create_chat_table()
            create_chat_ai_table()
        except Exception:
            raise
        logger.info("Database initialized")
        return 0

    if args.command == "add-user":
        user = add_account()
        logger.info("Added user %s", user["user_id"])
        return 0
    
    if args.command == "add-chat":
        print("Welcome to our Chat Application! \nMessage your loved ones with ease.")
        sender = input("\nEnter you username: ").title()
        if not check_user_in_db(sender):
            raise ValueError(f"{sender} is not found, consider adding an account.")
        
        receiver = input("Who do you want to chat with? ").title()
        if not check_user_in_db(receiver):
            raise ValueError(f"{receiver} is not found. contact support for this user or try connecting another user")
        chats = fetch_chats(sender=sender, receiver=receiver)
        print(f"Your chats with {receiver} loading....")
        time.sleep(2)
        if chats is None:
            print(f"No Chats between you and {receiver}")
            return 0
        for chat in chats:
            print(f"\n{chat}")

        chat = add_chat(sender=sender, receiver=receiver)
        logger.info("Chat sent %s", chat["chat_id"])
        return 0
    
    if args.command == "chat-ai":
        print("Welcome to our chat bot. \nInteractively chat with AI")
        name = input("\n\nPlease provide your username to continue: ")
        while True:
            message = input("\nInput your message. Or (q, Q, exit, ctrl+c) to stop the program: ")
            if message in ("q", "Q") or message.upper() in ("EXIT", "QUIT"):
                print("Exiting console.. bye!")
                return 0
            user_chat = add_chat_role_user(sender=name, message=message)
            logger.info("Chat sent. Waiting for response...")

            model_chat = add_chat_role_model(sender=name, message=user_chat["message"])
            logger.info("AI Response")
            print(f"\n\n{model_chat["ai_response"]}")

    parser.print_help()
    return 2


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    raise SystemExit(main())
