from src.validacoes import valor_positivo


def test_valor_positivo():
    assert valor_positivo(10.0) is True


def test_valor_zero_nao_e_positivo():
    assert valor_positivo(0.0) is False


def test_valor_negativo_nao_e_positivo():
    assert valor_positivo(-1.0) is False
