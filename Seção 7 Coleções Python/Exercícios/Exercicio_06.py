"""
Faça um programa que receba do usuário um vetor com 100 posições. Em seguida deverá ser impresso
o maior  eo menor elemento do vetor.
"""
import random
vetor = []
while len(vetor) < 10:
    valor = random.randrange(0, 100)
    vetor.append(valor)

print(vetor)
print(f' Maior Valor: {max(vetor)}')
print(f' Menor Valor: {min(vetor)}')
