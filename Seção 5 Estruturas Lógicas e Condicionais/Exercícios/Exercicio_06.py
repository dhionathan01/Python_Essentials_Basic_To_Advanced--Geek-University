"""
Faça um programa que receba dois números inteiros, mostre na tela qual o maior, e a diferença entre ele ambos.
"""
valor1 = float(input('Insira o 1° Número: '))
valor2 = float(input('Insira o 2° Número: '))

if valor1 > valor2:
    print(f'{valor1} é maior que {valor2}')
    dif = valor1 - valor2
    print(f'{valor1} - {valor2} = {dif} \nA diferença entre eles é igual a: {dif}')
elif valor2 > valor1:
    print(f'{valor2} é maior que {valor1}')
    dif = valor2 - valor1
    print(f'{valor2} - {valor1} = {dif} \nA diferença entre eles equivale: {dif}')

else:
    print(f'Erro : Os numeroes Inseridos Possui valores iguais \n{valor1} é igual a {valor2}')
