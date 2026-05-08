import pandas as pd
from pathlib import Path

def transform_data():
    input_path = Path("data/raw/alunos.csv")
    output_path = Path("data/processed/alunos.csv")

    df = pd.read_csv(input_path)

    df["nome_aluno"] = df["nome_aluno"].str.strip()
    df["genero"] = df["genero"].str.strip()
    df["serie"] = df["serie"].str.strip()
    df["turma"] = df["turma"].str.strip()

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False, encoding="utf-8")

    print(f"{len(df)} linhas transformadas.")

    return len(df)

if __name__ == "__main__":
    transform_data()