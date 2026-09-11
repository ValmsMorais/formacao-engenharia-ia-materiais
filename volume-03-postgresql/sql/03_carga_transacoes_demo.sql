WITH nova_importacao AS (
    INSERT INTO importacoes (
        nome_arquivo,
        finalizado_em,
        qtd_validas,
        qtd_rejeitadas
    )
    VALUES (
        'transacoes.csv',
        CURRENT_TIMESTAMP,
        5,
        0
    )
    RETURNING id
)
INSERT INTO transacoes (
    importacao_id,
    cliente_id,
    tipo,
    valor,
    ocorrida_em
)
SELECT i.id, c.id, v.tipo, v.valor, v.ocorrida_em
FROM nova_importacao i
CROSS JOIN (
    VALUES
        ('12345678901', 'CASHIN',  250.00::NUMERIC, TIMESTAMP '2026-09-01 10:15:00'),
        ('12345678901', 'CASHOUT',  80.50::NUMERIC, TIMESTAMP '2026-09-02 14:20:00'),
        ('23456789012', 'CASHIN', 1200.00::NUMERIC, TIMESTAMP '2026-09-03 09:05:00'),
        ('34567890123', 'CASHOUT', 300.75::NUMERIC, TIMESTAMP '2026-09-03 18:40:00'),
        ('23456789012', 'CASHOUT', 150.00::NUMERIC, TIMESTAMP '2026-09-04 11:30:00')
) AS v(documento, tipo, valor, ocorrida_em)
JOIN clientes c
  ON c.documento = v.documento;
