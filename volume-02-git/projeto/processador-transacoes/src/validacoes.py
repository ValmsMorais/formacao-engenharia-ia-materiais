from datetime import date, datetime


def valor_positivo(valor: float) -> bool:
    return valor > 0


def data_nao_futura(data_texto: str) -> bool:
    data_transacao = datetime.strptime(data_texto, "%Y-%m-%d").date()
    return data_transacao <= date.today()
