SELECT c.nome,
       COUNT(t.id) AS qtd_transacoes,
       COALESCE(SUM(t.valor),0) AS valor_total,
       MAX(t.ocorrida_em) AS ultima_movimentacao
FROM clientes c
LEFT JOIN transacoes t ON t.cliente_id = c.id
GROUP BY c.id, c.nome
ORDER BY valor_total DESC;
