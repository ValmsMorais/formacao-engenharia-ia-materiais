# Processador de Transações — Volume 01

Abra esta pasta no VS Code. Os caminhos abaixo partem dela, não da raiz do volume.

## Preparação

Crie e ative uma .venv conforme a seção 6.4 do livro. Depois:
```bash
python -m pip install -r requirements.txt
python -m src.main
```

O main.py inicial apenas mostra o caminho e a orientação da Sprint 1. Implemente as etapas nele; os módulos finais serão criados por você.

## Entradas e saídas

- Sprint 1: data/entrada/transacoes.csv, com 10 registros limpos.
- Sprint 2 em diante: mude ARQUIVO_ENTRADA para data/entrada/transacoes_com_erros.csv, com 8 registros e erros propositais.
- Trate falhas de conversão por linha para continuar o processamento.
- data/saida/ recebe validos.csv, rejeitados.csv, resumo.json e relatórios que você criará. .gitkeep apenas preserva a pasta.

## Testes

Execute `python -m pytest -q` nesta pasta. O test_placeholder.py só confirma que pytest funciona. Acrescente testes reais para valor, data, cliente e duplicidade.

## Continuidade

O material-base do Volume 02 usa o nome externo processador-transacoes. Aqui usamos processador_transacoes. O pacote Python é src em ambos. Siga o caminho indicado em cada livro; não apague sua implementação ao trocar de volume.
