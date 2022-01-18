"""
Faça um programa que receba 6 números inteiros e mostre:
* Os números pares digitados.
* A soma dos números pares digitados;
* A quantidade de números ímpares digitados
"""
from random import randint
vetor = []
while len(vetor) < 10:
    vetor.append(randint(0, 100))   # Gera um número aleatório de 0 a 100 e o coloca dentro do vetor
print(f'Números Inseridos: {vetor}')
vetor_numeros_pares = []
vetor_numeros_impares = []
for valor in vetor:
    if valor % 2 == 0:
        vetor_numeros_pares.append(valor)
    else:
        vetor_numeros_impares.append(valor)

print(f'Os números pares informados:\n {vetor_numeros_pares}\n'
      f'A soma dos números pares equivale: {sum(vetor_numeros_pares)}')
print(f'Os números Ímpares informados são: {vetor_numeros_impares}\n'
      f'Foram inseridos {len(vetor_numeros_impares)} números impares')
