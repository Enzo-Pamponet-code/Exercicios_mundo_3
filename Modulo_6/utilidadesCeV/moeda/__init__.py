def aumentar(preco, porcentagem, formate = True):
    preco = float(preco)
    porcentagem = float(porcentagem)
    if formate:
        return f'R$ {(preco + (preco * porcentagem/100)):.2f}'
    return preco + (preco * porcentagem/100)


def diminuir(preco, porcentagem, formate = True):
    preco = float(preco)
    porcentagem = float(porcentagem)
    if format:
        return f'R$ {(preco - (preco * porcentagem/100)):.2f}'
    return preco - (preco * porcentagem/100)


def metade(preco, formate = True):
    preco = float(preco)
    if formate:
        return f'R$ {(preco/2):.2f}'
    return preco


def resumo(preco, aumento,diminuicao, formate = True):
    print('-'*60)
    print(f'{"RESUMO DO VALOR":^60}')
    print('-'*60)
    preco = float(preco)
    aumento = preco + preco*aumento/100
    diminuicao = float(diminuicao)
    preco_f = f'R${preco:.2f}'
    aumento_f = f'R${aumento:.2f}'
    diminuito_f = f'R${diminuicao:.2f}'
    preco_d = f'R${2*preco:.2f}'
    preco_m = f'R${preco/2:.2f}'
    if formate:
        print(f'O valor analizado:\t\t{preco_f}')
        print(f'Aumento de {(aumento - preco) * 100 / preco}:\t\t{aumento_f}')
        print(f'Diminuição de {diminuicao}%:\t{diminuito_f}')
        print(f'Dobro de {preco_f}:\t\t{preco_d}')
        print(f'Metade de {preco_f}:\t\t{preco_m}')