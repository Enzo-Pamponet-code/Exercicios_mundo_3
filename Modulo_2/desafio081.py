lista= []
while True:
    numero = input('Digite um valor: ')
    if numero.isnumeric():
        lista.append(int(numero))
    else:
        break
lista.sort(reverse=True)
print(f'''Foram digitados: {len(lista)}
A ordem decrescente: {lista}''')
if 5 in lista:
    print(f'O valor 5 apareceu na lista ')
else:
    print('O 5 não foi digitado')
