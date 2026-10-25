from time import sleep
def contador(i,f,p=1):
    i = int(float(i))
    f = int(float(f)) + 1
    p = int(float(p))
    if i > f and p>0:
        p = int(-p)
    elif p == 0:
        p = 1
    print('-'*60)
    print(f'Contagem de {i} até {f-1} em {abs(p)} em {abs(p)}')
    if i > f:
        f -= 2
    for c in range(i,f,p):
        print(c, end=' ')
        sleep(0.5)
    print('FIM')


contador(1,10,1)
print('-'*60)
contador(10,0,2)
contador(10,0)
print('-'*60)
print('Agora é sua vez')
contador(input('Digite o inicio: '),input('Digite o fim: '),input('Digite o passo: '))
