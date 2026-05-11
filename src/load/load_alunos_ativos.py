from pathlib import Path
import sqlite3
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_PATH = PROJECT_ROOT / "data" / "processed" / "alunos_tratados.csv"
DB_PATH = PROJECT_ROOT / "db" / "alunos.sqlite"
TABLE_NAME = "alunos"

def load_data():
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Arquivo tratado não encontrado: {INPUT_PATH}")
    
    df = pd.read_csv(INPUT_PATH)

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_alunos_matricula
            ON alunos(matricula)
            """
        )

    print(f"{len(df)} linhas acarregada na tabela: {TABLE_NAME}")
    print(f"Bacno SQLite criado em: {DB_PATH}")

    return len(df)

if __name__ == "__main__":
    load_data()