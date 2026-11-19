from cupom import MAXIMO, desconto_valido


def test_aceita_percentual_exatamente_no_limite():
    # preparar
    percentual = MAXIMO
    # agir
    resultado = desconto_valido(percentual)
    # verificar
    assert resultado is True


def test_rejeita_percentual_acima_do_limite():
    percentual = MAXIMO + 1
    resultado = desconto_valido(percentual)
    assert resultado is False


def test_rejeita_percentual_zero():
    percentual = 0
    resultado = desconto_valido(percentual)
    assert resultado is False


def test_rejeita_percentual_nao_inteiro_dentro_da_faixa():
    percentual = MAXIMO - 0.5
    resultado = desconto_valido(percentual)
    assert resultado is False
