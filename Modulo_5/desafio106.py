from random import randint
def mini_sistema():
    while True:
        funcao = input('Função ou Biblioteca > ').strip().lower()
        if funcao == 'fim':
            break
        print('-'*30)
        print(f'Acessando o comando "{funcao}"')
        print('-'*30)
        print(f'\033[{randint(30,37)}m')
        help(funcao)
        print('\033[m')

mini_sistema()