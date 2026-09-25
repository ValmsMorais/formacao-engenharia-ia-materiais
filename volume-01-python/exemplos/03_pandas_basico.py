import pandas as pd

# Execute a partir da pasta volume-01-python.
df = pd.read_csv("dados/transacoes.csv")
print(df.head())
df.info()  # Mostra o resumo diretamente; retorna None.
