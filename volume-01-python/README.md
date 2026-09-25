# Volume 01 — Python para Engenharia de IA

Baixe o repositório pela opção Code > Download ZIP, extraia e abra volume-01-python no VS Code. A pasta deve conter diretamente dados, exemplos, exercicios, gabaritos, projeto e requirements.txt. Os programas das aulas usam esta pasta como diretório atual.

## Preparação
Leia GUIA_AMBIENTE.md e a seção 6.4 do PDF. Use uma .venv e instale:
```bash
python -m pip install -r requirements.txt
```
Dependências: pandas (tabelas) e pytest (testes). Módulos csv, json, logging e pathlib já acompanham Python.

## Mapa das aulas
- 5.2 CSV: `python exemplos/01_ler_csv.py`.
- 5.3 JSON: `python exemplos/02_json.py`, que lê dados/configuracao.json.
- 7.1 pandas: `python exemplos/03_pandas_basico.py`.
- 7.2 agrupamento: `python exemplos/04_pandas_analise.py`.
- 7.2 combinação: `python exemplos/05_merge_clientes.py`, usando dados/clientes.csv.

Depois de CSV, complete exercicios/01_total_transacoes.py. Depois de limpeza, complete exercicios/02_limpeza_pandas.py. Consulte os arquivos correspondentes em gabaritos somente após tentar.

## Projeto
Na Parte 9, abra projeto/processador_transacoes como pasta do VS Code. Siga seu README e execute `python -m src.main`. A Sprint 1 usa a entrada limpa; a Sprint 2 troca para a entrada com erros. Os módulos e relatórios finais são exercícios, não arquivos faltantes.

Todos os dados são fictícios.
