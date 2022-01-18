"""
Leia 10 números inteiros e aramzene em um vetor v.
Crie dois novos vetores v1 e v2.
Copie os valores ímpares de v para v1 e os valores pares de v para v2.
No final escreva os elementos Utilizados de v1 e v2
"""
from random import randint

v = []
v1 = []
v2 = []
for i in range(10):
    v.append(randint(0, 100))
print(v)

for valor in v:
    if valor % 2 != 0:
        v1.append(valor)
    else:
        v2.append(valor)

print(f'Valores Ímpares:\n {v1}')
print(f'Valores Pare:\n {v2}')
