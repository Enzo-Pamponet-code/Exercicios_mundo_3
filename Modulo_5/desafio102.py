from math import gamma

import sympy as sp
from sympy.codegen.ast import integer


def fatorial(f, show=False):
    """
    -> Calcula o fatorial de um número, se for o fatorial de um número quebrado, ele calcula a função gama
    :param f:  Número a ser calculado
    :param show: Mostrar o passo a passo
    :return: retorna o fatorial
    """
    #-------fatorial simples------------#
    if f == 0:
        if show:
            return f'0! = 1'
        return 1
    elif int(float(f)) == f:
        f = int(float(f))
        if f >0:
            n = 1
            for c in range(1,f+1):
                n *= c
            if show:
                p = ''
                for c in range(1,f+1):
                    if c ==1:
                        p += f'{c} '
                    else:
                        p += f'x {c} '
                return f'{p} = {n}'
            return n
        else:
            n = 1
            for c in range(-1,f-1,-1):
                n *= c
            if show:
                p = ''
                for c in range(-1, f - 1, -1):
                    if c == -1:
                        p += f'{c} '
                    else:
                        p += f'x {c} '
                return f'{p} = {n}'
            return n
    else:
        x = sp.Symbol('x')
        integral = sp.integrate(x**f * sp.exp(-x), (x, 0, sp.oo))
        if show:
            return f'gamma({f}) ~= {float(integral.evalf())}'
        return float(integral.evalf())

print((-4)**(1/2))
print(fatorial(100, show=True))