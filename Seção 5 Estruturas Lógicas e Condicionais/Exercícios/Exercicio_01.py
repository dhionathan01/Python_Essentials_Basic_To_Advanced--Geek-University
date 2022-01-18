"""
Faça um Programa que receba dois números e mostre qual dele é o maior
"""

numero1 = float(input('Insira o primeiro número: '))
numero2 = float(input('Insira o segundo número: '))

if numero1 > numero2:
    print(f'O maior número é : {numero1}')
elif numero2 > numero1:
    print(f'O maior número inserido foi: {numero2}')
else:
    print('Os números inseridos possuim o mesmo valor')