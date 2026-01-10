import sqlite3
import functools
from sqlite3 import Connection
from typing import Dict, List, Tuple, Optional


class DatabaseError(Exception):
    pass


def db_connection(func):
    """Decorator that opens a sqlite3 connection and ensures it's closed.

    The wrapped function receives the `Connection` as the first argument.
    Database errors are raised as `DatabaseError` for callers to handle.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn: Optional[Connection] = None
        try:
            conn = sqlite3.connect("chat_box.db")
            conn.row_factory = sqlite3.Row
            result = func(conn, *args, **kwargs)
            # Persist any changes made by the inner function
            conn.commit()
            return result
        except sqlite3.Error as exc:
            raise DatabaseError(str(exc))
        finally:
            if conn:
                conn.close()

    return wrapper


@db_connection
def create_table_users(connection: Connection) -> None:
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        username TEXT NOT NULL
    )
    """
    cursor.execute(query)


@db_connection
def save_users(conn: Connection, user_data: Dict[str, str]) -> str:
    """Insert a user record and return the user_id."""
    cursor = conn.cursor()
    user_id = user_data.get("user_id")
    username = user_data.get("username")
    if not user_id or not username:
        raise ValueError("user_data must include 'user_id' and 'username'")
    query = "INSERT INTO users (user_id, username) VALUES (?, ?)"
    cursor.execute(query, (user_id, username))
    return user_id


@db_connection
def fetch_users(connection: Connection) -> List[Tuple[str, str]]:
    """Return all users as a list of `(user_id, username)` tuples."""
    cursor = connection.cursor()
    query = "SELECT user_id, username FROM users"
    cursor.execute(query)
    rows = cursor.fetchall()
    return [(row[0], row[1]) for row in rows]


@db_connection
def create_chat_table(connection: Connection) -> None:
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS chat (
        chat_id TEXT PRIMARY KEY,
        message TEXT NOT NULL,
        sender TEXT NOT NULL,
        receiver TEXT NOT NULL
    )
    """
    cursor.execute(query)


@db_connection
def save_chat(conn: Connection, chat_data: Dict[str, str]) -> str:
    """Insert a chat message and return the chat_id."""
    cursor = conn.cursor()
    chat_id = chat_data.get("chat_id")
    message = chat_data.get("chat_message")
    sender = chat_data.get("sender")
    receiver = chat_data.get("receiver")
    if not all([chat_id, message, sender, receiver]):
        raise ValueError("chat_data must include 'chat_id','chat_message','sender','receiver'")
    query = "INSERT INTO chat (chat_id, message, sender, receiver) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (chat_id, message, sender, receiver))
    return chat_id


@db_connection
def fetch_chats(connection: Connection, sender: str, receiver: str) -> str:
    """ Fetch chat between to sender and the reciever"""

    cursor = connection.cursor()
    query = """
            SELECT chat_id, message
            FROM chat
            WHERE (sender = ? AND receiver = ?)
            OR (sender = ? AND receiver = ?)
            """

    data = (sender, receiver, receiver, sender)
    cursor.execute(query, data)
    response = cursor.fetchall()

    return [ row[1] for row in response]




