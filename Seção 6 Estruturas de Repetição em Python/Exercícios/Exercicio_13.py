"""
Faça um programa que leia um número inteiro positivo par N
e imprima todos os números pares de 0 até N em ordem crescente.
"""
N = int(input('Informe o número par: '))
lista = []
if N % 2 == 0 and N > 0:
    for i in range(0, N+1):
        if i % 2 == 0:
            lista.append(i)
    print(f'Lista de números pares de 0 a {N}:\n {lista}')
else:
    print('Número digitado não é um positivo par')


