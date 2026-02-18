from extract.extract_csv import extract
from transform.transform_data import transform
from load.load_postgres import load

def run():
    df = extract()
    df = transform(df)
    load(df)
    print("ETL finalizado com sucesso :rocket:")

if __name__ == "__main__":
    run()