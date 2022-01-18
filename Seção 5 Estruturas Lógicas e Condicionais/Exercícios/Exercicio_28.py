"""
Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias
conforme o valor numérico digitado pelo usuário:
a - Geométrica: Raíz cubica(x * y * z)
b - Ponderada: (x + 2y + 3 * z) / 6
c - Harmônica (1/x + 1/y + 1/z) / 1
d - Aritmética: (x + y + z) / 3
"""
from math import sqrt
calculo = input('Informe o calculo que deseja efetuar: \n'
                'a - Geométrico \n'
                'b - Ponderado \n'
                'c - Hârmonico \n'
                'd - Aritmético \n'
                ': ')
calculo = calculo.lower()
valores_validos = False
x = int(input('Informe o valor x: '))
y = int(input('Informe o valor y: '))
z = int(input('Informe o valor z: '))
if x > 0 and y > 0 and z > 0:
    valores_validos = True
total = 0
tipo = ''

if valores_validos:
    if calculo == 'a':
        tipo = 'Geométrica'
        total = sqrt(x * y * z)
    elif calculo == 'b':
        tipo = 'Ponderada'
        total = (x + 2 * y + 3 * z) / 6
    elif calculo == 'c':
        tipo = 'Hârmonica'
        total = (1 / x + 1 / y + 1 / z) / 1
    elif calculo == 'd':
        tipo = 'Aritmética'
        total = (x + y + z) / 3
    else:
        tipo = 'Opção escolhida não é válida'
        total = False
else:
    print('Um ou mais valores informados não é possitivo inteiro')

print(f'Operação: {tipo} em que x = {x} y = {y} z = {z}\n'
      f'Equivale: {total:.2f}')
