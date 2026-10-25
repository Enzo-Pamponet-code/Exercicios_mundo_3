from moeda import moeda_v2

p = float(input('Digite um número: R$ '))
print(f'Aumentando em 13% o {moeda_v2.moeda(p)} temos {moeda_v2.aumentar(p, 13)}')
print(f'Diminuindo em 10% o {moeda_v2.moeda(p)} temos {moeda_v2.diminuir(p, 10)}')
print(f'A metade de {moeda_v2.moeda(p)} é {moeda_v2.metade(p)}')
print(f'O dobro de {moeda_v2.moeda(p)} é {moeda_v2.dobro(p)}')