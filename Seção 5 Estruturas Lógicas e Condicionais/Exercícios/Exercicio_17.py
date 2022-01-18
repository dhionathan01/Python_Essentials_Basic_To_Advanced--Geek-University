"""
Faça um programa que calcule e mostre a área de um trapézio.
Sabe se que

A = base maior + base menor * altura / 2
A = area
"""
base_maior = float(input('Informe a base maior: '))
base_menor = float(input('Informe a base menor: '))
altura = float(input('Informe a altura: '))

A = ((base_maior + base_menor) * altura) / 2
print(f'A area do trapézio equivale a : {A}')

