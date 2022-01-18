"""
Leia um valor de massa em libras e apresente-o convertido em quilograms. A fórmula de conversão é:
K = L x 0,45, K a massa em quilograms e L a massa em libras
"""

L = float(input('Insira o valor em Libas: '))

K = L * 0.45

print(f'{L} lb equivale: {K} kg')
