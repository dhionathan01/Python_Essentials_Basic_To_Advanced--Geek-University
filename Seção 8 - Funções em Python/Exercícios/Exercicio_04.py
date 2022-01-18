"""
Faça uma função para verificar se um número é um quadrado perfeito.
Um quadrado perfeito é um número inteiro não negativo que pode ser expresso como o quadrado de outro número inteiro.
Exemplo: 1, 4, 9...
"""
from math import sqrt


def verificar_quadrado_perfeito(valor):
    if valor > 0:
        print(sqrt(valor))
        if sqrt(valor) // 1 == sqrt(valor):
            print('Quadrado perfeito')
        else:
            print('Não é um quadrado perfeito')

    else:
        print('O número deve ser positivo')


numero = int(input('Digite um número: '))
verificar_quadrado_perfeito(numero)
