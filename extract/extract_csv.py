import pandas as pd

def extract():
    # Simulando leitura de CSV
    data = [
        {"nome": "Ana", "idade": 28},
        {"nome": "Bruno", "idade": 35},
        {"nome": "Carla", "idade": 22},
    ]

    df = pd.DataFrame(data)
    print("Extract concluído")
    return df