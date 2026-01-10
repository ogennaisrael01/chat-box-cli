# Chat Box CLI

Lightweight command-line chat application with a simple SQLite-backed storage.

**Requirements**

- Python 3.8+

**Overview**

The application exposes a small CLI implemented in `chat/main.py`. It supports
three primary commands:

- `init-db` — create the required SQLite tables
- `add-user` — interactively add a user to the database
- `add-chat` — interactively send a chat message between two existing users

All commands are intended to be run from the repository root using the module
entry point. This ensures imports resolve correctly.

Usage examples (PowerShell):

```powershell
# Create and activate a virtual environment
python -m venv venv
& venv\Scripts\Activate.ps1

# Initialize the database (creates users and chats tables)
python -m chat.main init-db

# Add a user interactively
python -m chat.main add-user

# Start an interactive chat session (prompts for sender/receiver and message)
python -m chat.main add-chat
```

Behavior details

- `init-db` calls `create_table_users()` and `create_chat_table()` to create
  the necessary SQLite tables.
- `add-user` runs an interactive prompt (see `chat/users.py`) and will log the
  created user's `user_id` on success.
- `add-chat` prompts for a sender and a receiver. If either user is not found
  the command will raise a `ValueError` with guidance to add the missing user.
  If prior chats exist between the two users, they are displayed, then the
  interactive flow collects and persists a new chat message.

Logging and exit codes

- The top-level script configures `logging` at `INFO` level by default and
  exits with `0` on success or `2` if the CLI was invoked without a known
  subcommand.

Developer notes

- Recommended run method: `python -m chat.main <command>` from the project
  root so Python resolves the `chat` package correctly.
- The project uses SQLite for persistence; the database file is created in the
  project root (see `chat/storage.py`).

Next steps

- Add automated tests for `chat/users.py` and `chat/storage.py`.
- Consider splitting interactive flows into non-interactive functions to make
  them easier to test and to add a programmatic API in future.

Files of interest

- `chat/main.py` — CLI entrypoint
- `chat/users.py` — user management helpers
- `chat/storage.py` — persistence utilities
