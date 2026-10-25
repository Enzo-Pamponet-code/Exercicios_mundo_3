tupla = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')))
print(f'A tupla ficou {tupla}')
print(f'O nove apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O três apareceu na posição {tupla.index(3)+1}')
else:
    print(f'O três não apareceu')
n = 0
p = ''
for c in tupla:
    if c % 2 == 0:
        n += 1
        p += f'{c} '
p = p[:len(p)-1]
pares = p

print(f'Apareceu {n} números pares, que foram {pares}')
