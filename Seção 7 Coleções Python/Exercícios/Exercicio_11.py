"""
Faça um programa para preencher um vetor com 10 números reais, calcule e mostre a quantidade de números negativos
e a soma dos números positivos desse vetor.
"""
import random

vetor = []
numeros_negativos = []
numeros_positivos = []
while len(vetor) < 10:
    valor = random.randrange(-100, 100)
    print(valor)
    vetor.append(valor)
    if valor < 0:
        numeros_negativos.append(valor)
    else:
        numeros_positivos.append(valor)

print(f' Números Preenchidos: {vetor}')
print(f' Números Negativos: {numeros_negativos}')
print(f' Números Positivos: {numeros_positivos} \n')
print(f'\n Conclusão :')
print(f' Quantidade de Números Negativos {len(numeros_negativos)}')
print(f' Soma dos Números Positovs : {sum(numeros_positivos)}')
