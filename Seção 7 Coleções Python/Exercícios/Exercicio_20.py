"""
Escreva um programa que leia números inteiros no intervalo de [0,50] e os armazene em um vetor com posição 10.
Preencha um segundo vetor apenas com os números ímpares do primeiro vetor. improma os dois vetores, elementos por linha.
"""
from random import randrange

vetor1 = []
while len(vetor1) < 10:
    vetor1.append(randrange(0, 50))
vetor2 = []
for i in vetor1:
    if i % 2 != 0:
        vetor2.append(i)
contador = 0
print('Vetor 1: ')
while contador < len(vetor1):
    print(vetor1[contador], vetor1[contador+1])
    contador += 2
contador2 = 0
print('Vetor 2: ')

while contador2 < len(vetor2):
    if len(vetor2) > contador2+1:
        print(vetor2[contador2], vetor2[contador2+1])
        contador2 += 2
    else:
        print(vetor2[contador2])
        contador2 += 2