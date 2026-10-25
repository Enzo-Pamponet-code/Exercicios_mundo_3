def escreva(txt):
    tam = int(len(txt) + 4)
    print('~'*(len(txt)+4))
    print(f'{txt:^{tam}}')
    print('~'*(len(txt)+4))


escreva('GUSTAVO GUANABARA')
escreva('Curso de Pytho no Youtube')
escreva('CeV')