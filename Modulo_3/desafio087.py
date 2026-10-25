matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]
for linha in range(0,3):
    for coluna in range(0,3):
        numero = int(input('Digite um valor: '))
        matriz[linha][coluna] = numero
pares = 0
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[  {matriz[linha][coluna]}  ]',end='')
        if matriz[linha][coluna]%2==0:
            pares += matriz[linha][coluna]
    print()
print('-='*30)
maior = 0
for c in matriz[1]:
    if matriz[1].index(c) == 0:
        maior = c
    else:
        if c > maior:
            maior = c
coluna3 = 0
for linha in range(0,3):
    for coluna in range(0,3):
        if coluna == 2:
            coluna3 += matriz[linha][2]
print(f'A somar dos pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {maior}')
