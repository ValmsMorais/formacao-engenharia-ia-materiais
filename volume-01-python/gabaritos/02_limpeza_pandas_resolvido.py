import pandas as pd

df = pd.read_csv("dados/transacoes_com_erros.csv")
df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
df["data_convertida"] = pd.to_datetime(df["data"], errors="coerce")
print("Problemas antes da limpeza:")
print(df[df["valor"].isna() | df["data_convertida"].isna() | df["id_cliente"].isna()])
df = df.drop_duplicates(subset=["id"], keep="first")
print("
Apos remover IDs duplicados:")
print(df)
