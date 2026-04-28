import os
from pathlib import Path

import firebird.driver as fdb
from sqlalchemy import create_engine


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATABASE = PROJECT_ROOT / "dataset" / "BANCO_FIREBIRD.FB5"
DEFAULT_CLIENT_LIBRARY = r"C:\Program Files\Firebird\Firebird_5_0\fbclient.dll"

_CLIENT_LOADED = False


def load_firebird_client():
    global _CLIENT_LOADED

    if _CLIENT_LOADED:
        return

    client_library = os.getenv("FIREBIRD_CLIENT_LIBRARY", DEFAULT_CLIENT_LIBRARY)
    if client_library and Path(client_library).exists():
        fdb.load_api(client_library)

    _CLIENT_LOADED = True


def get_connection():
    load_firebird_client()

    user = os.getenv("FIREBIRD_USER", "SYSDBA")
    password = os.getenv("FIREBIRD_PASSWORD", "masterkey")
    host = os.getenv("FIREBIRD_HOST", "localhost")
    port = os.getenv("FIREBIRD_PORT", "3055")
    database = Path(os.getenv("FIREBIRD_DATABASE", str(DEFAULT_DATABASE)))

    if not database.is_absolute():
        database = PROJECT_ROOT / database

    engine = create_engine(
        f"firebird+firebird://{user}:{password}@{host}:{port}/{database.as_posix()}"
    )
    return engine.connect()
