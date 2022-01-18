"""
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer correspondentes
a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições
X e Y.
"""
import random
vetor = []
for i in range(8):
    valor = random.randrange(0, 100)
    vetor.append(valor)
print(f'Lista de Valores Gerados: {vetor}')

posicao_1 = int(input('Digite a 1° Posição desejada : '))
posicao_2 = int(input('Digite a 2° Posição desejada : '))
soma = vetor[posicao_1] + vetor[posicao_2]
print(f'Resultado Soma das Posições: {soma}')
