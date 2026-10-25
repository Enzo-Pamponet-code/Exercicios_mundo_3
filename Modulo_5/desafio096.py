def area(largura,altura):
    print(f'O terreno tem {largura} metros de largura e {altura} metros de altura que equivale a uma área de {largura*altura} metros quadrados')


print('CONTROLE DE TERRENO')
print('-'*60)
largura = float(input('Largura(m): '))
altura = float(input('Altura(m): '))
area(largura,altura)