import csv
import os
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

import psycopg

ARQUIVO = Path("dados/transacoes_com_erros.csv")
DSN = os.environ["PSYCOPG_DSN"]

TIPOS_ACEITOS = {"CASHIN", "CASHOUT"}


def validar(linha: dict) -> tuple[bool, str | None, Decimal | None, datetime | None]:
    documento = (linha.get("documento") or "").strip()
    tipo = (linha.get("tipo") or "").strip().upper()

    if not documento:
        return False, "documento ausente", None, None

    if tipo not in TIPOS_ACEITOS:
        return False, f"tipo invalido: {tipo}", None, None

    try:
        valor = Decimal((linha.get("valor") or "").strip())
    except InvalidOperation:
        return False, "valor invalido", None, None

    if valor <= 0:
        return False, "valor deve ser positivo", None, None

    try:
        ocorrida_em = datetime.fromisoformat((linha.get("ocorrida_em") or "").strip())
    except ValueError:
        return False, "data/hora invalida", None, None

    return True, None, valor, ocorrida_em


with psycopg.connect(DSN) as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO importacoes (nome_arquivo)
            VALUES (%s)
            RETURNING id
            """,
            (ARQUIVO.name,),
        )
        importacao_id = cur.fetchone()[0]

        validas = 0
        rejeitadas = 0

        with ARQUIVO.open(newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for numero_linha, linha in enumerate(leitor, start=2):
                ok, motivo, valor, ocorrida_em = validar(linha)

                if not ok:
                    cur.execute(
                        """
                        INSERT INTO rejeicoes (
                            importacao_id,
                            linha,
                            conteudo,
                            motivo
                        )
                        VALUES (%s, %s, %s, %s)
                        """,
                        (importacao_id, numero_linha, str(linha), motivo),
                    )
                    rejeitadas += 1
                    continue

                cur.execute(
                    "SELECT id FROM clientes WHERE documento = %s",
                    (linha["documento"],),
                )
                cliente = cur.fetchone()

                if cliente is None:
                    cur.execute(
                        """
                        INSERT INTO rejeicoes (
                            importacao_id,
                            linha,
                            conteudo,
                            motivo
                        )
                        VALUES (%s, %s, %s, %s)
                        """,
                        (
                            importacao_id,
                            numero_linha,
                            str(linha),
                            "cliente nao encontrado",
                        ),
                    )
                    rejeitadas += 1
                    continue

                cur.execute(
                    """
                    INSERT INTO transacoes (
                        importacao_id,
                        cliente_id,
                        tipo,
                        valor,
                        ocorrida_em
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        importacao_id,
                        cliente[0],
                        linha["tipo"].upper(),
                        valor,
                        ocorrida_em,
                    ),
                )
                validas += 1

        cur.execute(
            """
            UPDATE importacoes
            SET finalizado_em = CURRENT_TIMESTAMP,
                qtd_validas = %s,
                qtd_rejeitadas = %s
            WHERE id = %s
            """,
            (validas, rejeitadas, importacao_id),
        )

print(f"Importacao concluida: {validas} validas; {rejeitadas} rejeitadas.")
