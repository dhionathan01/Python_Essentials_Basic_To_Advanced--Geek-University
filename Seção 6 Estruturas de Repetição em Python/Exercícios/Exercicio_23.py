"""
Faça um algoritmo que leia um número positivo e imprima os seus divisores.
"""
divisores = []
valor = int(input('Insira o valor: '))
if valor > 0:
    for i in range(1, valor+1):
        if valor % i == 0:
            divisores.append(i)

print(f'Os divisores de {valor} são: {divisores}')