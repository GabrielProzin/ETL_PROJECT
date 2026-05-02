from pathlib import Path
import sqlite3

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_PATH = PROJECT_ROOT / "data" / "processed" / "vendas_tratadas.csv"
DB_PATH = PROJECT_ROOT / "db" / "vendas.sqlite"
TABLE_NAME = "vendas"


def load_data():
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Arquivo tratado nao encontrado: {INPUT_PATH}")

    df = pd.read_csv(INPUT_PATH)

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_vendas_data_pagamento
            ON vendas(data_pagamento)
            """
        )

    print(f"{len(df)} linhas carregadas na tabela '{TABLE_NAME}'.")
    print(f"Banco SQLite criado em: {DB_PATH}")

    return len(df)


if __name__ == "__main__":
    load_data()