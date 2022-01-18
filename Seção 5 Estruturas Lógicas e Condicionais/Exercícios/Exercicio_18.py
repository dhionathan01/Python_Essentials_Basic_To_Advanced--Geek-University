"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo).
O usuário escolhe uma das operações e o seu programa então pede dois valores numéricos e realiza a operação
mostrano o resultado e saindo.
"""
operacao = input(''
                 'Adição  " + " \n'
                 'Subtração  " - " \n'
                 'Divisão  "/" \n'
                 'Multiplicação  "*" \n'
                 'Escolha a operação desejada: ')
valor1 = float(input('Informe o valor 1: '))
valor2 = float(input('Informe o valor 2: '))

if operacao == '+' or operacao == 'adição' or operacao == 'Adição':
    total = valor1 + valor2
    print(f'{valor1} + {valor2} : {total}')
elif operacao == '-' or operacao == 'subtração' or operacao == 'Subtração':
    total = valor1 - valor2
    print(f'{valor1} / {valor2} : {total}')
elif operacao == '*' or operacao == 'multiplicação' or operacao == 'Multiplicação':
    total = valor1 * valor2
    print(f'{valor1} x {valor2} : {total}')
elif operacao == '/' or operacao == 'divisão' or operacao == 'Divisão':
    total = valor1 / valor2
    print(f'{valor1} / {valor2} : {total}')