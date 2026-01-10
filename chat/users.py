from typing import Optional, Tuple, Dict
from storage import save_users, fetch_users
import uuid


def to_dict(user_data: str) -> Dict[str, str]:
    """Convert the provided user data into a dict with a username key."""
    return {"username": user_data}


def add_account() -> Dict[str, str]:
    """Interactively create and persist a user account.

    Returns the created user dict.
    """
    username = input("Enter your username: ").strip()
    if not username or username.isdigit():
        raise ValueError("Only non-empty alphabetic usernames are allowed")

    username = username.title()
    user_data = to_dict(username)
    user_data.update({"user_id": str(uuid.uuid4())})
    save_users(user_data=user_data)
    return user_data


def check_user_in_db(user_name: str) -> bool:
    """Return True if `user_name` exists in the database."""
    users = fetch_users()
    for _, name in users:
        if name == user_name:
            return True
    return False


def get_user_by_username(username: str) -> Optional[Tuple[str, str]]:
    """Return a `(user_id, username)` tuple or None if not found."""
    users = fetch_users()
    for user in users:
        if user[1] == username:
            return user
    return None


    

    


