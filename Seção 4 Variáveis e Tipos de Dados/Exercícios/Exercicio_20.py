"""
Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é L = K / 0.45
K = massa em quilogramas
L = massa em Libras
"""
K = float(input('Digite o valor em quilogramas: '))
L = (K / 0.45)
print(f'{K} Kg equivale a {L:.2f} Libras')

