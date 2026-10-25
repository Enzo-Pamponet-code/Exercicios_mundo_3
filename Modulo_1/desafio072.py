tupla = ('zero','um','dois','três','quatro','cinco','seis',
         'sete','oito','nove','dez','onze','doze',
         'treze','quatorze','quinze','dezesseis','dezessete',
         'dezoito','dezenove','vinte')
while True:
    number = int(input('Digite um número entre 0 e 20: '))
    if 0 <= number < 21:
        print(f'Você digitou o número {tupla[number]}')
        continuar = input('''Quer continuar?
[1] Sim
[2] Não
''')
        if continuar == '2':
            break
    else:
        print('Tente novamente!')