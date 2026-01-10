import argparse
import logging
from users import add_account
from storage import create_table_users, create_chat_table


logger = logging.getLogger(__name__)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="chat_box")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("init-db", help="Create the database tables")
    sub.add_parser("add-user", help="Interactively add a user")

    args = parser.parse_args(argv)

    if args.command == "init-db":
        create_table_users()
        create_chat_table()
        logger.info("Database initialized")
        return 0

    if args.command == "add-user":
        user = add_account()
        logger.info("Added user %s", user["user_id"])
        return 0

    parser.print_help()
    return 2


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    raise SystemExit(main())
from users import add_account
from storage import create_table_users



def main():
    print("Welcome to Our Chat box")

    print("If you wish to continue, press 0. otherwise  press 1")

    choice = int(input())

    if choice == 1:
        return "Good bye"
    
    elif choice == 0:
        print("Please Enter your username to continue")
        create_table_users()
        add_account()


if __name__ == "__main__":
    print(main())
