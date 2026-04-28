from sqlalchemy import text
from pathlib import Path
from db.conexao_db import get_connection
import csv

QUERY_PATH = Path(__file__).resolve().parent / "queries" / "vendas.sql"

def read_query():
    return QUERY_PATH.read_text(encoding="utf-8")

def extract_data():
    query = read_query()

    with get_connection() as conn:
        result = conn.execute(text(query))

        rows = result.fetchall()
        columns = result.keys()
    
    
    print(columns)
    print(rows[:5])

    output_path = Path("data/raw/vendas.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(rows)

    return len(rows)






if __name__ == "__main__":
    extract_data()
