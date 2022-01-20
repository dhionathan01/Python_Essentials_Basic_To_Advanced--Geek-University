"""
Faça um algoritmo que receba um número inteiro positivo n e calcule o seu fatorial, n!
"""


def fatorial(valor):
    resultado = 1
    for multiplicar in range(valor, 1, -1):
        resultado *= multiplicar
    return resultado


n = int(input('Insira o valor que deseja encontrar o fatorial: '))
print(f'{n}! = {fatorial(n)}')