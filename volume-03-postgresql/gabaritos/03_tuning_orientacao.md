# Orientação - Exercício 03: tuning

Não existe um único plano correto: o resultado depende do volume e das estatísticas.

Um caminho de referência:

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT *
FROM transacoes
WHERE cliente_id = 2
  AND ocorrida_em >= TIMESTAMP '2026-09-01 00:00:00'
  AND ocorrida_em <  TIMESTAMP '2026-10-01 00:00:00';
```

O schema do volume já inclui o índice:

```sql
CREATE INDEX idx_transacoes_cliente_data
    ON transacoes (cliente_id, ocorrida_em DESC);
```

Compare:
- tipo de acesso escolhido;
- `cost` estimado;
- linhas estimadas versus reais;
- `actual time`;
- buffers lidos/atingidos.

Para observar diferença de forma mais evidente, aumente o conjunto de dados. Em tabelas pequenas, um `Seq Scan` pode continuar sendo a melhor escolha e isso não é erro.
