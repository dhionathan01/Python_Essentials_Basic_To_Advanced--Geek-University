"""
Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais
"""
N = int(input('Informe o valor:'))
soma = 0
for i in range(0, N+1):
    soma = soma + i

print(f"A soma de todos os números de 0 a {N} equivale: {soma}")