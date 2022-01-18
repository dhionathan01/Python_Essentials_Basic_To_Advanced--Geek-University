"""
Faça um programa que leia dos vetores de 10 posições
e calcule outro vetor contendonas posições pares os valores do primeiro
e nas posições impares os valores do segundo
"""
from random import randint

vetor1 = []
vetor2 = []
vetor3 = []
contador = 0
while len(vetor1) < 10:
    vetor1.append(randint(0, 100))
    vetor2.append(randint(0, 100))
    vetor3.append(vetor1[contador])
    vetor3.append(vetor2[contador])
    contador += 1
print(f'vetor1:\n{vetor1}')
print(f'vetor2:\n{vetor2}')
print(f'vetor3:\n{vetor3}')
