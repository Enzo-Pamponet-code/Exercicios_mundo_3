def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
            return f'você digitou o número {num}'
        except ValueError:
            print('\033[31mDigite um numero inteiro valido:\033[m')
            continue


n =leiaint('Digite um numero inteiro: ')
print(n)