import moeda

p = float(input('Digite um número: R$ '))
print(f'Aumentando em 13% o {p} temos {moeda.aumentar(p,13)}')
print(f'Diminuindo em 10% o {p} temos {moeda.diminuir(p, 10)}')
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')