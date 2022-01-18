"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os pares de 0 até N em ordem descrescente.
"""
N = int(input('Insira o Número: '))
if N % 2 == 0 and N > 0:
    for i in range(N, 0, -1):
        if i % 2 == 0:
            print(i)
else:
    print('Número informado não é um positivo par')
