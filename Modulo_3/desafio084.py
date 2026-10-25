lista_composta = []
lista = []
while True:
    nome = input('Nome: ')
    peso = int(input('Peso: '))
    lista.append(nome)
    lista.append(peso)
    lista_composta.append(lista[:])
    lista.clear()
    if input('Quer continuar? [S/N] ') in'Nn':
        break
print(f'Foram {len(lista_composta)} pessoas cadastradas.')
maior = menor = 0
for c in lista_composta:
    if lista_composta.index(c) == 0:
        maior = menor = c[1]
    else:
        if c[1] > maior:
            maior = c[1]
        elif c[1] < menor:
            menor = c[1]
listam = []
listan = []
for c in lista_composta:
    if c[1] == maior:
        listam.append(c[0])
    if c[1] == menor:
        listan.append(c[0])
# Dava para colocar a comparação do maior e do menor dentro do while
print(f'O maior peso foi de {maior} kg e foi de: {listam}')
print(f'O menor peso foi de {menor} kg e foi de: {listan}')