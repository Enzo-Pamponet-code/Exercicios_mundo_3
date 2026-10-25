lista = [[],[]]
for c in range(0,7):
    num = int(input(f'Digite um numero para a posição {c+1}: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print('-='*30)
print(f'Os valores pares foram: {lista[0]}')
print(f'Os valores ímpares foram: {lista[1]}')