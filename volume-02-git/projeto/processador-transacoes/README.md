# Processador de Transações

Projeto-base do Volume 02. Antes de iniciar as sprints, copie esta pasta inteira para um local de estudos fora do repositório de materiais. Execute `git init` somente na cópia.

Entrada inicial: `data/entrada/transacoes.csv`.

A pasta `data/saida/` começa sem resultados e receberá os arquivos produzidos pelo programa. O arquivo `.gitkeep` existe apenas para que o Git consiga preservar a pasta vazia.

## Arquivos de ambiente

- `.gitignore`: impede o versionamento de ambiente virtual, cache, logs e do arquivo `.env` real.
- `.env.example`: modelo seguro que pode ser versionado. Não coloque senhas ou tokens nele.
- `requirements.txt`: dependências necessárias para executar os testes e continuar o projeto.

## Testes

Na raiz desta cópia do projeto:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

O arquivo `pytest.ini` mantém a importação do pacote `src` consistente também quando `pytest -q` é usado diretamente.

Este README é propositalmente inicial. Na Sprint 2, use `templates/README_PROJETO.md` como roteiro e transforme-o em uma documentação completa.
