"""
Faça um programa que leia um número inteiro positivo par N
e imprima todos so números naturais de 0 até N em ordem decrescente.
"""
N = int(input('Insira o valor: '))
if N > 0:
    lista = []
    for i in range(N, 0, -1):
        lista.append(i)

    print(f'Lista números de 0 a {N} decrescente: \n {lista}')
else:
    print('Número informado não é positivo')

