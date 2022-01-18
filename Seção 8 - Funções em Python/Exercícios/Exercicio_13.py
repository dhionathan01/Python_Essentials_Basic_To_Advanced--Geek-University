"""
Faça uma função que receba dois valores númericos e um símbolo. Este símbolo represetara a operação que se deseja
efetuar com números. Se o símbolo for + deverá ser realizada uma adição, se for - uma subtração, se for / uma divisão
e se for * será efetuada multiplicação.
"""


def realiza_calculo(valor1, valor2, operacao):
    if operacao == '+':
        print(f'{valor1} + {valor2} = {valor1 + valor2}')
    elif operacao == '-':
        print(f'{valor1} - {valor2} = {valor1 - valor2}')
    elif operacao == '*':
        print(f'{valor1} x {valor2} = {valor1 * valor2}')
    elif operacao == '/':
        print(f'{valor1} % {valor2} = {valor1 / valor2}')
    else:
        print('Opção Inválida')


num1 = float(input('Informe o primeiro valor: '))
calculo = input('Informe:\n'
                '+ para somar\n'
                '- para subtrair\n'
                '* para multiplicar\n'
                '\ para dividir\n')
num2 = float(input('Informe o segundo valor: '))
realiza_calculo(valor1=num1, valor2=num2, operacao=calculo)
