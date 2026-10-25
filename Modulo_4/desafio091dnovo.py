from time import sleep
from random import randint
from operator import itemgetter
dicionario = {}
for c in range(1, 5):
    dicionario[f'jogador{c}'] = randint(1, 6)
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print('Valores sorteados:')
print('-='*30)
for k, v in dicionario.items():
    sleep(1)
    print(f'  {k} tirou {v} no dado.')
print('-='*30)
print('Ranking dos jogadores:')
rodada = 1
for k, v in ranking:
    sleep(1)
    print(f'  {rodada}° {k} tirou {v} no dado.')
    rodada += 1