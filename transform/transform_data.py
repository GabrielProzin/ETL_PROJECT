def transform(df):
    df["idade_em_10_anos"] = df["idade"] + 10
    print("Transform concluído")
    return df