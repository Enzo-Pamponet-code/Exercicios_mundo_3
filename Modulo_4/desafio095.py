dicionario = dict()
lista = list()
while True:
    dicionario['nome'] = input('Nome do jogador: ')
    gols = []
    for c in range(0, int(input(f'Quantas partidas {dicionario["nome"]} jogou: '))):
        gol = int(input(f'Quantos gols {dicionario["nome"]} fez na {c+1}° partida: '))
        gols.append(gol)
    dicionario['gols'] = gols[:]
    total = 0
    for g in gols:
        total += g
    dicionario['total'] = total
    lista.append(dicionario.copy())
    dicionario.clear()
    gols.clear()
    if input('Deseja continuar? [S/N]: ') in 'Nn':
        break
print(lista)
print('-=-' * 20)
print(f'{"n":>4} {"nome"} {'gols':^30} {'total':<30}')
print('-'*60)
for p, c in enumerate(lista):
    tots = str(c['gols'])
    print(f'{p:>4} {c["nome"]:<15} {tots:<20} {c["total"]}')
while True:
    print('-' * 60)
    dados = int(input('Mostrar dados de qual jogador?: '))
    if dados == 999:
        break
    if dados >= len(lista):
        print('Erro')
    else:
        print(f'--Levantamento do jogador {lista[dados]}--:')
        for c, g in enumerate(lista[dados]['gols']):
            print(f'  No jogo {c+1} fez {g} gols')