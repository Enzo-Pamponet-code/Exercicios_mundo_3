def notas(*n, caso=False):
    """
    Uma função que cria um dicionário com vários dados seguindo como base as notas dos alunos
    :param n: Números que representam notas dos alunos
    :param caso: Se True, mostra a situação do aluno, se False, não mostra
    :return: Retorna um dicionário
    """
    di = dict()
    di['total'] = len(n)
    di['maior'] = max(n)
    di['menor'] = min(n)
    di['media'] = float(f'{sum(n)/len(n):.2f}')
    if caso:
        if di['media'] >= 7:
            di['situação'] = 'Boa'
        elif di['media'] >= 5:
            di['situação'] = 'Razoável'
        else:
            di['situação'] = 'Ruim'
    return di


print(notas(1,2,3, caso=True))

