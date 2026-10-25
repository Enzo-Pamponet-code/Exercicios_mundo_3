lista_completa = []
while True:
    numero = int(input('Digite um número: '))
    sim_nao = input('Deseja continuar? [S/N]').strip().upper()[0]
    lista_completa.append(numero)
    if sim_nao == 'N':
        break
lista_pares = []
lista_impares = []
for c in lista_completa:
    if c % 2 == 0:
        lista_pares.append(c)
    else:
        lista_impares.append(c)
print('lista completa:',lista_completa)
print('lista de pares:',lista_pares)
print('lista de ímpares:',lista_impares)