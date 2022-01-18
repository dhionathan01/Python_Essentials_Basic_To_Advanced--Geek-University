"""
Faça um programa que leia um número inteiro positivo impar N
e imprima todos os números ímapres de 1 até N em ordem crescente.
"""
N = int(input('Informe o valor: '))
if not N % 2 == 0 and N > 0:
    for i in range(0, N+1):
        if not i % 2 == 0:
            print(i)
else:
    print('O número informado não é positivo impar')
