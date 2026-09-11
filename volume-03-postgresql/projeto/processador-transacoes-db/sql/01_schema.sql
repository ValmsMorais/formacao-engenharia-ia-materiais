CREATE TABLE clientes (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    documento VARCHAR(14) NOT NULL UNIQUE,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE importacoes (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome_arquivo VARCHAR(255) NOT NULL,
    iniciado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finalizado_em TIMESTAMP,
    qtd_validas INTEGER NOT NULL DEFAULT 0,
    qtd_rejeitadas INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE transacoes (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    importacao_id BIGINT NOT NULL REFERENCES importacoes(id),
    cliente_id BIGINT NOT NULL REFERENCES clientes(id),
    tipo VARCHAR(10) NOT NULL CHECK (tipo IN ('CASHIN','CASHOUT')),
    valor NUMERIC(14,2) NOT NULL CHECK (valor > 0),
    ocorrida_em TIMESTAMP NOT NULL
);

CREATE TABLE rejeicoes (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    importacao_id BIGINT NOT NULL REFERENCES importacoes(id),
    linha INTEGER NOT NULL,
    conteudo TEXT NOT NULL,
    motivo TEXT NOT NULL
);

CREATE INDEX idx_transacoes_cliente_data
    ON transacoes (cliente_id, ocorrida_em DESC);
