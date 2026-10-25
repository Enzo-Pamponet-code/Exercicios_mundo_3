dicionario = dict()
lista = list()
while True:
    nome = input('Digite seu nome: ')
    while True:
        sexo = input('Digite seu sexo (M/F): ').upper()[0]
        if sexo in 'MF':
            break
    idade = int(input('Digite sua idade: '))
    dicionario['nome'] = nome
    dicionario['sexo'] = sexo
    dicionario['idade'] = idade
    lista.append(dicionario.copy())
    dicionario.clear()
    while True:
        pergunta =input('Deseja continuar? [S/N]')[0]
        if pergunta in 'Nn':
            break
        elif pergunta in 'Ss':
            continue
        else:
            print('Digite apenas S ou N')
    if pergunta in 'Nn':
        break
print(f'-Foram cadastradas {len(lista)} pessoas.')
media = 0
mulheres = ''
for c in lista:
    media += c['idade']
    if c['sexo'] == 'F':
        mulheres += f'{c['nome']} '
print(f'-A media de idade do grupo é {media / len(lista)} anos')
print(f'-As mulheres cadastradas foram {mulheres}')
print(f'-As pessoas com a idade acima da média foram: ')
for c in lista:
    if c['idade'] > media/len(lista):
        print()
        print(f'nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]} ')
print('Encerrado')