import os
from pathlib import Path, PureWindowsPath

import firebird.driver as fdb


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATABASE = PROJECT_ROOT / "dataset" / "BANCO_FIREBIRD.FB5"
DEFAULT_CLIENT_LIBRARY = r"C:\Program Files\Firebird\Firebird_5_0\fbclient.dll"

_CLIENT_LOADED = False


def is_absolute_database_path(database_path):
    return (
        Path(database_path).is_absolute()
        or PureWindowsPath(database_path).is_absolute()
    )


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
    host = os.getenv("FIREBIRD_HOST")
    port = os.getenv("FIREBIRD_PORT")
    database = os.getenv("FIREBIRD_DATABASE", str(DEFAULT_DATABASE))

    if host:
        database_dsn = database
    else:
        if not is_absolute_database_path(database):
            database = PROJECT_ROOT / database
        database_dsn = Path(database).as_posix()

    if host:
        database_dsn = f"{host}/{port}:{database_dsn}" if port else f"{host}:{database_dsn}"

    return fdb.connect(
        database=database_dsn,
        user=user,
        password=password,
        charset="UTF8",
    )
