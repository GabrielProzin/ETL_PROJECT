from config.database import get_engine

def load(df):
    engine = get_engine()
    df.to_sql("pessoas", engine, if_exists="replace", index=False)
    print("Load concluído")