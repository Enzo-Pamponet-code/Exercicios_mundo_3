from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10),randint(1, 10), randint(1, 10))
print(f'o valores obtidos da tupla foram {tupla}')
maior = 0
menor = 0
for n, c in enumerate(tupla)   :
    if n == 1:
        maior = menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
print(f'''maior: {maior}
menor: {menor}
''')