import csv
from pathlib import Path

arquivo_csv = Path("dados/transacoes.csv")
with arquivo_csv.open(newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        valor = float(linha["valor"])
        print(linha["id"], linha["tipo"], valor)
