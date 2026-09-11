import json
from pathlib import Path

arquivo = Path("dados/configuracao.json")
config = json.loads(arquivo.read_text(encoding="utf-8"))
print(config["valor_revisao"])
print(config["tipos_aceitos"])
