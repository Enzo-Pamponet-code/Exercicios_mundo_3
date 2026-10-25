from random import randint
from time import sleep
def sorteio(lst):
    print('Fazendo o sorteio dos 5 valores temos: ', end=' ')
    for i in range(0, 5):
        sleep(1)
        a = randint(1, 10)
        lst.append(a)
        print(a, end=' ')
    print('Pronto!')



def soma(lst):
    lst2 = 0
    for c in lst:
        sleep(1)
        if c % 2 == 0:
         lst2 += c
    print(f'Somando os valores pares de {lst}, temos {lst2}')


lista = []
sorteio(lista)
soma(lista)