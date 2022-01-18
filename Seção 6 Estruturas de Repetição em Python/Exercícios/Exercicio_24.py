"""
Escreva um programa que leia um número inteiro e calcule a soma de todos so divisores desse número,
com exceção dele próprio. Ex: a soma dos divisores do número 66 é:
 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""
divisores = []
valor = int(input('Insira o valor: '))
if valor > 0:
    for i in range(1, valor+1):
        if valor % i == 0 and valor != i:
            divisores.append(i)
print(f'A soma dos divisores de {valor} equivale: {sum(divisores)}')
