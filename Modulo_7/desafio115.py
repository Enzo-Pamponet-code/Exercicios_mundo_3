import desafio115 as d
from time import sleep
try:
    while True:
        lista = []
        d.print_('Menu Principal')
        o = d.opcoes('Ver pessoas cadastradas','Cadastrar novas pessoas','Sair do sistema')
        print('-'*50)
        desejo = d.numput('\033[33mSua opção:\033[m ')
        i = d.analizador(desejo, o)
        if i == 3:
            print('Saindo do sistema...')
            break
        d.dados(i,lista)
        sleep(2)
except KeyboardInterrupt:
    print('\nPrograma interrompido pelo usuario')