from random import randint
from time import sleep
lista = []
dados = []
print('_'*30)
print(f'{'Jogo da Mega-Sena':^30}')
print('-'*30)
num = int(input('Quantos jogos deseja gerar: '))
for c in range(0,num):
    for i in range(0,6):
        numero = int(randint(1, 60))
        while True:
            if numero in dados:
                numero = int(randint(1,60))
            else:
                break
        dados.append(numero)
    dados.sort()
    lista.append(dados[:])
    dados.clear()
print('-'*15,f'Sorteando {len(lista)} jogos','-'*15)
for p, o in enumerate(lista):
    sleep(2)
    print(f'Jogo {p+1}: {o}')
print('-'*15,'<Boa Sorte>','-'*15)
