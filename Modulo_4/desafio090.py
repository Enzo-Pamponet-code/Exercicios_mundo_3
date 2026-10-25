pretexto = {}
nome = input('Qual é o nome do aluno?: ')
pretexto['Nome'] = nome
media = float(input('Digite sua média: '))
pretexto['Media'] = media
if media >= 7:
    pretexto['Situação'] ='Aprovado'
else:
    pretexto['Situação'] = 'Reprovado'
print('-'*40)
for k, v in pretexto.items():
    print(f'-{k} é igual a {v}')