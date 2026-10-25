def voto(ano):
    from datetime import date
    atual = date.today().year - ano
    obr = f'com {atual} anos: VOTO OBRIGATORIO'
    opc = f'com {atual} anos: VOTO OPCIONAL'
    if atual > 65:
        return opc
    elif atual > 18:
        return obr
    else:
        return opc


print(voto(int(input('Digite o ano de nascimento: '))))