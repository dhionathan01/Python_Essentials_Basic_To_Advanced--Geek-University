"""
Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou por 5,
mas não simultaneamente pelos dois
"""
valor = float(input('Insira o valor a ser verificado: '))

if valor % 5 == 0 and not valor % 3 == 0:
    print(f'{valor} Divisível por 5 mas não por 3 ')
elif valor % 3 == 0 and not valor % 5 == 0:
    print(f'{valor} Divisível por 3 mas não por 5 ')
else:
    print(f'{valor} Divisível por ambos tanto 3 quanto 5')
