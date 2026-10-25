lista = []
expressao = input('Digite um expressão matemática: ')
for c in expressao:
    lista.append(c)
if lista.count('(') == lista.count(')'):
    lista_aberta = []
    lista_fechado = []
    for p, c in enumerate(lista):
        if c == '(':
            lista_aberta.append(p)
        elif c == ')':
            lista_fechado.append(p)
    if lista_aberta[0] > lista_fechado[0] or lista_aberta[-1] > lista_fechado[-1]:
        print('Expressão invalida')
    else:
        print('Expressão valida')
else:
    print('Expressão invalida')