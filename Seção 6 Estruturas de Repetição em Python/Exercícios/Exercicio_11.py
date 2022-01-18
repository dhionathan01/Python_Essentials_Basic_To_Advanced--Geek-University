"""
Faça um programa que leia um número inteiro positivo N
e imprima todos os números naturais de 0 até N em ordem crescente
"""
N = int(input('Insira o valor: '))
if N > 0:
    lista = []
    for i in range(0, N+1):
        lista.append(i)

    print(f'Números naturais inteiros de 0 a {N}:\n {lista}')
else:
    print('Número informado não é positivo')
