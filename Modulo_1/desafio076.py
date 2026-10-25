tupla = ('Lápis', 1.75,'Borracha', 2, 'Caderno', 15.90)
print('-'*40)
print(f'{"Listagem de produtos":^40}')
print('-'*40)
for c in range(0,len(tupla)):
    if c % 2 == 0:
        print(f'{tupla[c] :-<30} R$ {float(tupla[c + 1]) :.2f}')
print('-'*40)
