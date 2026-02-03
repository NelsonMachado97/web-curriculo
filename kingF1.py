import requests
import pandas as pd

# 1. Buscar a última sessão realizada (onde há mais chance de ter dados)
url_sessions = "https://api.openf1.org/v1/sessions?year=2023"
sessions = requests.get(url_sessions).json()

if not sessions:
    print("❌ Nenhuma sessão encontrada para este ano.")
else:
    # Pegamos a última sessão da lista
    session_key = sessions[-1]['session_key']
    session_name = sessions[-1]['session_name']
    print(f"✅ Tentando sessão: {session_name} (Key: {session_key})")

    # 2. Buscar telemetria (Car Data)
    # Vamos aumentar o limite para 100 e não filtrar por piloto ainda
    url_car = f"https://api.openf1.org/v1/car_data?session_key={session_key}&limit=100"
    car_data = requests.get(url_car).json()

    if not car_data:
        print("⚠️ A API retornou uma lista vazia para esta sessão. Tentando outra...")
    else:
        df_car = pd.DataFrame(car_data)
        print("✅ Dados encontrados!")
        print(f"Colunas disponíveis: {df_car.columns.tolist()}")
        print("\n--- Primeiras 5 linhas ---")
        print(df_car.head())