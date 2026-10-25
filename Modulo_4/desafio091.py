from random import randint
from time import sleep
dicionario = {}
l_ord = []
lista = []
slista = []
input('')
for c in range(0, 4):
    jogador = f'jogador{c + 1}'
    numero = randint(1, 6)
    slista.append(jogador)
    slista.append(numero)
    lista.append(slista[:])
    slista.clear()
for c in lista:
    if len(l_ord) == 0:
        l_ord.append(c)
    else:
        for p in range(0, len(l_ord)):
            if c[1] <= l_ord[p][1]:
                l_ord.insert(p, c )
                break
            else:
                if p == len(l_ord)-1:
                    l_ord.append(c)
                    break
                else:
                    if c[1] <= l_ord[p+1][1]:
                        l_ord.insert(p+1, c)
                        break
l_ord = l_ord.copy()[::-1]
for c in l_ord:
    dicionario[c[0]] = c[1]
print('Valores sorteados: ')
for c in lista:
    sleep(1)
    print(f'   {c[0]} tirou {c[1]}')
print('Ranking dos jogadores: ')
rodada = 1
for k, v in dicionario.items():
    sleep(1)
    print(f'   {rodada}° {k} tirou {v}')
    rodada += 1
