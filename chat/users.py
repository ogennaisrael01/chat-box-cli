from storage import save_users, fetch_users
import uuid

def to_dict(user_data: str) -> dict:
    """
    Convert the provided user data into a dict
    """
    return {
        "username": user_data
    }


def add_account():
    username = input("Enter your username: ")

    if username.isdigit():
        return "only strings are allowed for usernames"

    username.title()

    user_data = to_dict(username)
    user_data.update({
        "user_id": str(uuid.uuid4())
    }
    )
    print(user_data)
    save_users(user_data=user_data)
    

    return f"User {user_data["user_id"]} saved"


def check_user_in_db(user_name):
    users = fetch_users()
    for user in users:
        if user[1] == user_name:
            return True
        
        else:
            return False

def get_user_by_username(username):
    users = fetch_users()
    for user in users:
        user_name = user[1]
        if user_name == username:
            return user
        
    return False


    

    


