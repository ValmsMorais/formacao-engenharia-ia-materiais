SELECT * FROM clientes WHERE ativo IS TRUE ORDER BY nome;
SELECT * FROM transacoes ORDER BY valor DESC LIMIT 3;
SELECT tipo, SUM(valor) total FROM transacoes GROUP BY tipo;
SELECT * FROM transacoes WHERE valor > 200 ORDER BY valor DESC;
