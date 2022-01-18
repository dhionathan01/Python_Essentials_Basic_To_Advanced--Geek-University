"""
Faça uma função que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro.
O volume de um cilindro circular é calculado por meio da seguinte fórmula:
V = pi * raio(quadrado) * altura, onde pi = 3,141 592
"""


def calc_volume_cilindro(raio_cilindro, altura_cilindro):
    pi = 3.141592
    V = pi * (raio_cilindro ** 2) * altura_cilindro
    return V


raio = float(input('Informe o raio do cilindro: '))
altura = float(input('Informe a altura do cilindro: '))
print(f'O volume do cilindro equivale: {calc_volume_cilindro(raio_cilindro=raio,altura_cilindro=altura)}')
