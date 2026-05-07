import pandas as pd
from pathlib import Path

def transform_data():
    input_path = Path("data/raw/alunos.csv")
    output_path = Path("data/processed/alunos.csv")

    df = pd.read_csv(input_path)

    