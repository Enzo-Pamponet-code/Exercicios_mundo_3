matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = c = 0
for linha in range(0,3):
    for coluna in range(0,3):
        numero = int(input(f'Digite um valor para posição {linha},{coluna}: '))
        if numero % 2 == 0:
            par += numero
        if coluna == 2:
            c += numero
        matriz[linha][coluna] = numero
print('-='*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()
print('-='*30)
print(f'A soma dos pares é: {par}')
print(f'A soma dos valores da terceira coluna: {c}')
print(f'O maior valor da 2° linha: {max(matriz[1])}')