def moeda(numero):
    numero = float(f'{numero:.2f}')
    parte_int = int(numero)
    parte_voadora = f'{numero - int(numero):.2f}'
    return f'R${parte_int},{str(parte_voadora)[-2:]}'


def aumentar(preco, porcentagem):
    preco = float(preco)
    porcentagem = float(porcentagem)
    f = moeda(preco + (preco * porcentagem/100))
    return f'{f}'


def diminuir(preco, porcentagem):
    preco = float(preco)
    porcentagem = float(porcentagem)
    return f'{moeda((preco - (preco * porcentagem/100)))}'


def metade(preco):
    preco = float(preco)
    return f'{moeda(preco)}'


def dobro(preco):
    return moeda(preco*2)
