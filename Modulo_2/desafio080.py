lista = []
for w in range(0,5):
    numero = input('Digite um número: ')
    numero = int(numero)
    if len(lista) == 0:
        lista.append(numero)
        print('colocado no final da lista')
    else:
        for c in range(0,len(lista)):
            if numero <= lista[c]:
                lista.insert(c, numero)
                print(f'colocado na posição {c} da lista')
                break
            else:
                if c == len(lista)-1:
                    lista.append(numero)
                    print(f'colocado na posição {c+1} da lista')
                else:
                    if numero <= lista[c+1]:
                        lista.insert(c+1, numero)
                        print(f'colocado na posição {c+1} da lista')
                        break
print('-=-'*20)
print(lista)