#já tinha feito antes :)
def leiaint(msg:str)-> int:
    num = 0
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31mDecidiu parar o programa\033[m')
            num = 0
            break
        except ValueError:
            print(f'\033[31mDigite um numero inteiro valido:\033[m')
            continue
        else:
            break
    return num


def leiafloat(msg:str)-> float:
    num = 0.0
    while True:
        try:
            num = float(input(msg))
        except KeyboardInterrupt:
            print('\033[31mDecidiu parar o programa\033[m')
            num = 0
            break
        except ValueError:
            print(f'\033[31mDigite um numero real valido:\033[m')
            continue
        else:
            break
    return num


n =leiaint('Digite um numero inteiro: ')
r =leiafloat('Digite um numero real valido: ')
print(f'O numero inteiro digitado foi {n} e o numero real digitado foi {r} .')