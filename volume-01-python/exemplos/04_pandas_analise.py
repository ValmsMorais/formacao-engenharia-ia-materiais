import pandas as pd

df = pd.read_csv("dados/transacoes.csv")
resumo = (df.groupby("tipo", as_index=False)
            .agg(quantidade=("id", "count"), total=("valor", "sum"), media=("valor", "mean")))
print(resumo)
