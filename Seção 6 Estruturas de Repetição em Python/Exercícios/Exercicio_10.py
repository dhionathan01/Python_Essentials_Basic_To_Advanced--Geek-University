"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
"""

soma = 0
contador = 0
lista = []
lista_pares = []
for i in range(1000):
    lista.append(i)
    if i % 2 != 0:
        soma = soma + 0

    else:
        soma = soma + i
        contador = contador +1
        lista_pares.append(i)
    if contador >= 50:
        break

print(f'Lista de números:\n {lista}')
print(f'Lista de números Pares:\n {lista_pares}')
print(f'Soma da Lista Total: {sum(lista)}')
print(f'Soma da Lista de Pares : {sum(lista_pares)}')
