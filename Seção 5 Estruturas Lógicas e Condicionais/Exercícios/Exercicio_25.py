"""
Calcule a equação segundo grau informando os valores de a, b, c
"""
from math import sqrt
a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

delta = b**2 - (4*a*c)
if delta < 0:
    print('Não existe raiz!')
elif delta == 0:
    print('Raíz Única')
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    print(f'x1: {x1} x2: {x2}')
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'x1: {x1:.2f} x2: {x2:.2f}')
