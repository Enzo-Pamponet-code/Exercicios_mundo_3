lista = []
aluno_notas = []
notas = []
rodada = 1
while True:
    nome = input(f'Qual o nome do(a) {rodada}° aluno(a)? ')
    nota1 = float(input('Digite a primeira nota dele(a): '))
    nota2 = float(input('Digite a segunda nota dele(a): '))
    notas.append(nota1)
    notas.append(nota2)
    notas.append((nota1+nota2)/2)
    aluno_notas.append(nome[:])
    aluno_notas.append(notas[:])
    lista.append(aluno_notas[:])
    notas.clear()
    aluno_notas.clear()
    rodada+=1
    if input('Quer continuar? [S/N]') in 'Nn':
        break
print(f'No. NOME  {'Média':^28}')
print('-'*30)
for p, n in enumerate(lista):
    numero = 21 - len(n[0]) -len(str(p))
    print(f'{p}   {n[0]}{lista[p][1][2]: {numero}}')
while True:
    print('-'*30)
    aluno = int(input('Mostrar nota do(a) aluno(a)? (999 interrompe): '))
    if aluno == 999:
        break
    print(f'Notas de {lista[aluno][0]} são [{lista[aluno][1][0]}, {lista[aluno][1][1]}]')

print('-='*30,f'Volte sempre!','-='*30)

