from datetime import datetime
dicionario = {}
nome = input('Digite o nome seu nome: ')
dicionario['nome'] = nome
ano = int(input('Digite o ano de nascimento: '))
atual =datetime.today().year - ano
dicionario['idade'] = atual
ctps = int(input('Digite o número da carteira de trabalho (0 não tem): '))
dicionario['ctps'] = ctps
if ctps > 0:
    acontrato = int(input('Digite seu ano de contrato: '))
    tc = datetime.today().year - acontrato
    dicionario['contratação'] = acontrato
    salario = int(input('Digite seu sálario: R$ '))
    dicionario['sálario'] = salario
    dicionario['Aposentadoria'] = 35 - tc  + atual
print('-='*30)
for k, v in dicionario.items():
    print(f'-- {k} tem o valor {v}')