# Chat Box CLI

Lightweight command-line chat example with a small SQLite-backed storage.

Features
- Create and persist users
- Persist chat messages between users
- Small, well-typed codebase suitable for learning and extension

Requirements
- Python 3.8+

Quick start

1. Create a virtual environment and activate it (Windows PowerShell):

```powershell
python -m venv venv
& venv\Scripts\Activate.ps1
```

2. Initialize the database:

```powershell
python -m chat.main init-db
```

3. Add a user:

```powershell
python -m chat.main add-user
```

Project layout

- `chat/` — package with modules: `storage.py`, `users.py`, `chat.py`, `main.py`
- `chat_box.db` — SQLite database created by `init-db`

Notes for developers
- The code uses a small `db_connection` decorator that opens and closes the SQLite
	connection and raises `DatabaseError` on failure.
- Functions return structured types and raise `ValueError` for invalid input.

Next steps
- Add unit tests for `users` and `storage` modules.
- Add a non-interactive API (HTTP) if desired.
