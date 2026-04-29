import pandas as pd
import csv
from pathlib import Path

def transform_data():
    
    input_path = Path("data/raw/vendas.csv")
    output_path = Path("data/processed/vendas_tratadas.csv")

    df = pd.read_csv(input_path)

    df["nome_aluno"] = df["nome_aluno"].str.strip()
    df["nome_responsavel"] = df["nome_responsavel"].str.strip()
    df["produto"] = df["produto"].str.strip()
    df["forma_pagamento"] = df["forma_pagamento"].str.strip()
    
    df["forma_pagamento"] = df["forma_pagamento"].str.replace(r"\s*/\s*$", "", regex=True)

    df["desconto"] = pd.to_numeric(df["desconto"], errors="coerce").fillna(0)
    df["valor_venda"] = pd.to_numeric(df["valor_venda"], errors="coerce").fillna(0)

    df["data_pagamento"] = pd.to_datetime(
        df["data_pagamento"].astype(str),
        format="%Y%m%d",
        errors="coerce"
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False, encoding="utf-8")

    print(f"{len(df)} linhas transformadas.")
    
    return len(df)

if __name__ == "__main__":
    transform_data()