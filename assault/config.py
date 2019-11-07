import os
from functools import lru_cache
from sqlalchemy import create_engine

@lru_cache(maxsize=32)
def engine(db_url=None):
    db_url = db_url or os.getenv("DB_URL")
    if not db_url:
        raise ValueError("database URL is required")
    print(f"Returning an engine for {db_url}")
    return create_engine(db_url)


def get_connection(db_url=None):
    return engine(db_url).connect()