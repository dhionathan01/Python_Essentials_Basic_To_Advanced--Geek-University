"""
Faça um programa que leia um valor N inteiro e positivo, calcule e moreste o valor de E, conforme a fórmula:
E = 1 + 1/1! + 1/2! + 1/3! + 1/4! + 1/N!
"""
from math import factorial
n = int(input('Informe o valor de N: '))
contador = 1
resultado = 0
if n > 0:
    while contador < n:
        resultado += 1/factorial(contador)
        contador += 1
else:
    print('Valor tem de ser positivo')
    exit()
print(f'Valor de E em sequência {n} equivale: {resultado:.2f}')

