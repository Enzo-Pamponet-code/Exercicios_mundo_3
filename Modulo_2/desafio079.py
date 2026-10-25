print('\033[31mQuando quiser sair escreva %sair% \033[m')
lista = []
while True:
    numero = input('Digite um número: ')
    if numero == '%sair%':
        break
    elif numero.isnumeric():
        if int(numero) in lista:
            print('Número já listado')
        else:
            numero = int(numero)
            lista.append(numero)
    else:
        print('Algo errado, tente novamente. ', end='')
print('-='*30)
print(sorted(lista))