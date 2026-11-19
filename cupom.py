MAXIMO = 22  # TROQUE pelo seu LIMITE


def desconto_valido(percentual):
    if percentual != int(percentual):
        return False
    if percentual <= 0:
        return False
    return percentual <= MAXIMO
