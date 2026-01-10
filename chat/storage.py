import sqlite3
import functools
from sqlite3 import Connection

def db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect("chat_box")
            if not connection:
                return "Faild to connect ot database"
            
            response = func(connection, *args, **kwargs)
            return response
        except sqlite3.Error as exc:
            return f"Database error: {str(exc)}"
        
    return wrapper


@db_connection
def create_table_users(connection: Connection):
    try:
        cursor = connection.cursor()

        query = """
            CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            username TEXT
        )
        """

        cursor.execute(query)

        connection.commit()
    except sqlite3.Error as exc:
        return f"Failed to create table 'user': {str(exc)}"
    
    return "Tablse 'users' Created Successfully.."



@db_connection
def save_users(conn: Connection, user_data: dict):

    cursor = conn.cursor()
    user_id = user_data.get("user_id", None)

    user_name = user_data.get("username", None)

    query = "INSERT INTO users (user_id, username) VALUES (?, ?)"

    # user data in tuple
    data = (user_id, user_name)
    try:
        # Exceute query and commit query
        cursor.execute(query, data)
        conn.commit()
    except sqlite3.Error as exc:
        print(str(exc))
        return f"Error while saving user: {str(exc)}"
    return f"Inserted {str(user_id)} user ID INTO database"

@db_connection
def fetch_users(connection: Connection):
    cursor = connection.cursor()

    query = "SELECT * FROM users"

    try:
        cursor.execute(query)

        response = cursor.fetchall()
    except sqlite3.Error as exc:
        print(str(exc))
        return f"Error fetching user data: {str(exc)}"
    for data in response:
        yield data


@db_connection
def create_chat_table(connection: Connection):
    cursor = connection.cursor()

    query = """ CREATE TEBLE IF NOT EXISTS chat (
        chat_id INTERGER PRIMARY KEY,
        message TEXT,
        sender TEXT,
        receiver TEXT
    )"""

    try:
        cursor.execute(query)

        connection.commit()
    except sqlite3.Error as exc:
        return f"Error occured while creating 'chat' table "
    
    return f"'chat' table created successfully"







