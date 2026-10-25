def numput(str_='Digite um número: ',str1='Digite novamente'):
    while True:
        try:
            num = input(str_)
            if int(float(num)) == float(num):
                return int(num)
            else:
                return float(num)
        except ValueError:
            print(f'\033[31m{str1}\033[m')


def licionario(nome, idade, lista:list):
    lista = lista
    di = dict()
    di['nome'] = nome
    di['idade'] = idade
    lista.append(di)


def printador(lista:list,str0='anos'):
    s = ''
    for c in lista:
        for d in c.values():
            if c['nome'] == d:
                s += f'{d:<30}'
            else:
                s += f'{d:>3} {str0}\n'
    return s


def print_(palavra, tam=60):
    print('-'*tam)
    print(f'{palavra:^{tam}}')
    print('-'*tam)


def opcoes(*opcao):
    po = 0
    for p, o in enumerate(opcao):
        print(f'{p+1}- \033[34m{o}\033[m')
        po = p+1
    return po


def analizador(num, opcao):
    if num > opcao or num <= 0:
        print('\033[31mErro\033[m')
        return IndexError
    else:
        return num


def dados(opcao,lista:list):
    try:
        open('dados.txt', 'r')
    except FileNotFoundError:
        open('dados.txt', 'a')
    if opcao == 1:
        texto = open('dados.txt', 'r')
        print_('Pessoas Cadastradas')
        print(texto.read())
        texto.close()
    elif opcao == 2:
        a = input('Nome: ')
        b = input('Idade: ')
        licionario(a, b, lista)
        texto = open('dados.txt', 'a')
        texto.write(printador(lista))
        print(f'Novo registro de {a} adicionado com sucesso!')
        texto.close()