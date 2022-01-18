"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = Raíz quadrada (Quadrado(a) + Quadrado(b).
Faça uma função que recaba os valores de 'a' e 'b' e calcule o valor da hipotenusa
"""
from math import sqrt


def calcular_hipotenusa(a, b):
    hipotenusa = sqrt((a ** 2) + (b ** 2))
    return hipotenusa


cateto_a = float(input('Informe o valor do cateto maior: '))
cateto_b = float(input('Informe o valor do cateto menor: '))
print(f'Valor da hipotenusa equivale:{calcular_hipotenusa(cateto_a, cateto_b)}')
