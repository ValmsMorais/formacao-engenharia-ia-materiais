import pandas as pd

transacoes = pd.read_csv("dados/transacoes.csv")
clientes = pd.read_csv("dados/clientes.csv")
resultado = transacoes.merge(clientes, on="id_cliente", how="left")
print(resultado[["id", "nome", "tipo", "valor"]].head())
