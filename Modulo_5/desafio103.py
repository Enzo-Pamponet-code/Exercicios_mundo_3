def ficha(nome = '<desconhecido>', gols = 0):
    if type(gols) == str :
        gols = 0
    elif gols.isnumeric():
        gols = int(gols)
    if nome.strip() == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gols'


#----------programa principal------------------
print(ficha(input('Qual o nome do jogador: '),input('Quantos gols na partida? ')))