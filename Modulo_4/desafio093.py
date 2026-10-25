dicionario = dict()
print('-=' * 30)
nome = input('Digite o nome do jogador: ')
dicionario['jogador'] = nome
partidas = int(input('Quantas partidas ele jogou: '))
dicionario['Partida'] = partidas
total =0
gol = []
for c in range(0, partidas):
    tota =  int(input(f'Quantos gols na partida {c+1}: '))
    gol.append(tota)
    total += tota
dicionario['Total'] = total
dicionario['Gols'] = gol
dicionario['Aproveitamento'] = total/ partidas
print('-=' * 30)
print(dicionario)
print('-=' * 30)
for c,p in dicionario.items():
    print(f'o campo {c} tem o valor {p}')
print('-=' * 30)
print(f'O jogador fez {partidas} partidas.')
for p, c in enumerate(gol):
    print(f'=> Na partida {p+1}, fez {c} gols.')
print(f'Foi um total de {total} gols.')