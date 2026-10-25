from moeda import moeda_v3

p = float(input('Digite um número: R$ '))
print(f'Aumentando em 13% de {moeda_v3.moeda(p)} temos {moeda_v3.aumentar(p, 13, formate=True)}')
print(f'Diminuindo em 10% de {moeda_v3.moeda(p)} temos {moeda_v3.diminuir(p, 10, formate=True)}')
print(f'A metade de {moeda_v3.moeda(p)} é {moeda_v3.metade(p, formate=True)}')