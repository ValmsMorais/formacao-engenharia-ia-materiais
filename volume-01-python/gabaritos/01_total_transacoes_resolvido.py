import csv

quantidade = 0
total = 0.0
maior = 0.0
with open("dados/transacoes.csv", newline="", encoding="utf-8") as arquivo:
    for linha in csv.DictReader(arquivo):
        valor = float(linha["valor"])
        quantidade += 1
        total += valor
        maior = max(maior, valor)
print(f"Quantidade: {quantidade}")
print(f"Total: {total:.2f}")
print(f"Maior: {maior:.2f}")
