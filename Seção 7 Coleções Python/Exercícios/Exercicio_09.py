"""
Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa.
"""
import random

vetor = []
while len(vetor) < 6:
    valor = random.randrange(0, 100)
    print(valor)
    if valor % 2 == 0:
        vetor.append(valor)

print(vetor)
print(f'Valores na Ordem Inversa: {vetor[::-1]}')
