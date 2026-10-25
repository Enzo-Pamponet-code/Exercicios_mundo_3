num =[]
print('-_'*30)
print(f'{'\033[31;40mLista de números\033[m':^60}')
print('-_'*30)
for c in range (0,5):
    num.append(int(input(f'Digite um número para posição {c}: ')))
maior = max(num)
menor = min(num)
print('-'*60)
lista_maior = []
lista_menor = []
for p, c in enumerate(num):
    if c == maior:
        lista_maior.append(p)
    elif c == menor:
        lista_menor.append(p)
print(f'A lista completa: {num}')
print(f'O maior valor foi: {maior} e o sua posição foi: {lista_maior}')
print(f'O menor valor foi: {menor} e sua posição foi: {lista_menor}')