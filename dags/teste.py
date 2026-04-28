from sqlalchemy import text

from db.conexao_db import get_connection


def list_user_tables():
    query = text(
        """
        SELECT rdb$relation_name
        FROM rdb$relations
        WHERE rdb$system_flag = 0
        """
    )

    with get_connection() as conn:
        return [row[0].strip() for row in conn.execute(query)]


if __name__ == "__main__":
    for table_name in list_user_tables():
        print(table_name)
