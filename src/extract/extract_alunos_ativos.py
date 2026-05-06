from pathlib import Path
from db.conexao_db import get_connection
import csv

QUERY_PATH = Path(__file__).resolve().parent / "queries" / "alunos.sql"

def read_query():
    return QUERY_PATH.read_text(encoding="utf-8")

def extract_data():
    query = read_query()

    output_path = Path("data/raw/alunos.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)


        columns = [field[0].lower() for field in cursor.description]

        with output_path.open("w", newline="", encoding="utf-8") as file:
            
            writer = csv.writer(file)
            writer.writerow(columns)

            while True:
                rows = cursor.fetchmany(1000)

                if not rows:
                    break

                writer.writerows(rows)

    return len(rows)

if __name__ == "__main__":
    extract_data()