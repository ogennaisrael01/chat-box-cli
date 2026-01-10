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
