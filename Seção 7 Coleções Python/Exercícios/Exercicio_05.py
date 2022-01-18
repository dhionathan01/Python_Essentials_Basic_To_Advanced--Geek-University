"""
Leia um vetor de 10 posições. Contar e Escrever quantos valores pares ele possui.
"""
import random
vetor = []
vetor_par = []
for i in range(10):
    valor = random.randrange(0, 100)
    vetor.append(valor)
print(vetor)

for i in range(10):
    if vetor[i] % 2 == 0:
        vetor_par.append(vetor[i])
print(f'Quantidade de valores pares: {len(vetor_par)}')
print(f'Valores Pares:{vetor_par}')
