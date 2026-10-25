from time import sleep
def maior(*numeros):
    lista = []
    for n in numeros:
        lista.append(n)
    print('-'*60)
    print('Analisando os valores passados...')
    for n in lista:
        print(n, end=' ')
        sleep(1)
    print(f'foram informados {len(lista)}')
    sleep(1)
    print(f'O maior valor foi {max(lista)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)



