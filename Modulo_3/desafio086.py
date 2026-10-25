matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]
for c in range(0,3):
    for p in range(0,3):
        num = int(input(f'Digite um numero para {c, p}: '))
        matriz[c][p].append(num)
print('-='*30)
print(f'[ {matriz[0][0][0]:^5} ] [ {matriz[0][1][0]:^5} ] [ {matriz[0][2][0]:^5} ]')
print(f'[ {matriz[1][0][0]:^5} ] [ {matriz[1][1][0]:^5} ] [ {matriz[1][2][0]:^5} ]')
print(f'[ {matriz[2][0][0]:^5} ] [ {matriz[2][1][0]:^5} ] [ {matriz[2][2][0]:^5} ]')