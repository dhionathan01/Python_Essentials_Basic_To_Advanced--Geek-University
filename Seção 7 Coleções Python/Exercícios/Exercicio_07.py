"""
Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento ea posição
que ele se encontra.
"""

import random

vetor = []

while len(vetor) < 10:
    valor = random.randrange(0, 100)
    vetor.append(valor)

print(vetor)
maior = max(vetor)
print(f'Maior Número: {maior}')
print(f'Posição onde o Valor se encontra: {vetor.index(maior)}')
