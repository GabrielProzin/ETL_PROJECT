from db.conexao_db import get_connection


def list_user_tables():
    query = """
        SELECT rdb$relation_name
        FROM rdb$relations
        WHERE rdb$system_flag = 0
        """

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return [row[0].strip() for row in cursor.fetchall()]


if __name__ == "__main__":
    for table_name in list_user_tables():
        print(table_name)
