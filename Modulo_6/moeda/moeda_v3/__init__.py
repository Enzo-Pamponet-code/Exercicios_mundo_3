def moeda(numero):
    numero = float(f'{numero:.2f}')
    parte_int = int(numero)
    parte_voadora = f'{numero - int(numero):.2f}'
    return f'R${parte_int},{str(parte_voadora)[-2:]}'



def aumentar(preco, porcentagem, formate = False):
    preco = float(preco)
    porcentagem = float(porcentagem)
    if formate:
        return moeda(preco + (preco * porcentagem/100))
    return preco + (preco * porcentagem/100)


def diminuir(preco, porcentagem, formate = False):
    preco = float(preco)
    porcentagem = float(porcentagem)
    if formate:
        return moeda(preco - (preco * porcentagem/100))
    return preco - (preco * porcentagem/100)


def metade(preco, formate = False):
    preco = float(preco)
    if formate:
        return moeda(preco/2)
    return preco/2