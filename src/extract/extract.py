from sqlalchemy import text

from db.conexao_db import get_connection


def extract_data():
    query = text(
        """
        SELECT FIRST 10 *
        FROM TBDUPLICATA
        """
    )

    with get_connection() as conn:
        rows = conn.execute(query).fetchall()

    for row in rows:
        print(row)

    return len(rows)
