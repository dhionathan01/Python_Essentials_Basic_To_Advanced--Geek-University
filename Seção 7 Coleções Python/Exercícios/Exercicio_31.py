"""
Faça um programa que leia dois vetores de 10 elementos.
Crie um vetor que seja a união entre os 2 vetores anteriores, ou seja, que contém os números dos dois vetores.
Não deve conter números repetidos.
"""
lista1 = []
lista2 = []
lista_uniao = []

while len(lista1) < 10:
    valor = int(input(f'Insira o {len(lista1)+1}° valor da lista1: '))
    lista1.append(valor)
    if valor not in lista_uniao:
        lista_uniao.append(valor)

while len(lista2) < 10:
    valor = int(input(f'Insira o {len(lista2) + 1}° valor da lista2: '))
    lista2.append(valor)
    if valor not in lista_uniao:
        lista_uniao.append(valor)

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'Lista União: {lista_uniao}')
