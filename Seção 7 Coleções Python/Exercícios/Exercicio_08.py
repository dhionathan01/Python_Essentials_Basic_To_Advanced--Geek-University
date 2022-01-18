"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.
"""
import random
vetor = []

while len(vetor) < 6:
    valor = random.randrange(0, 100)
    vetor.append(valor)
print(vetor)
print(f'Ordem inversa:\n {vetor[::-1]}')
