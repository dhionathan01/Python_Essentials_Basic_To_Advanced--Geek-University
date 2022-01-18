"""
Leia 10 números inteiros e armazene em um vetor.
Em seguida escrava os elementos que são primos e as suas respetivas posições no vetor
"""
from random import randint

lista_de_numeros = []
lista_de_numeros_primos = []

while len(lista_de_numeros) < 10:
    lista_de_numeros.append(randint(0, 100))

print(f'Numeros inseridos:\n {lista_de_numeros}')
multiplicavel = 0
for valor in lista_de_numeros:
    contador_de_multiplos = 0

    for verificador in range(2, valor):
        if valor % verificador == 0:
            contador_de_multiplos += 1

    if contador_de_multiplos <= 0 and valor != 0:
        lista_de_numeros_primos.append(valor)

for valor in lista_de_numeros_primos:
    print(f'O valor {valor} pertênce ao índice: {lista_de_numeros.index(valor)}')