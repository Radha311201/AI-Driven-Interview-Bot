from typing import Any


def get_session() -> Any:
    raise NotImplementedError("Database session not configured. Implement app/db/session.py")
