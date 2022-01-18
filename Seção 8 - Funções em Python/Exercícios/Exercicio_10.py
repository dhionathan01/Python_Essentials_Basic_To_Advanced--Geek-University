"""
Faça uma função que recaba dois números e retorne qual é o maior:
"""


def maior_inserido(valor1, valor2):
    if valor1 > valor2:
        return f'O maior valor inserido foi: {valor1}'
    elif valor2 > valor1:
        return f'O maior valor inserido foi: {valor2}'
    else:
        return 'Os valores, são iguais'


num1 = float(input('Informe o 1° valor: '))
num2 = float(input('Informe o 2° valor: '))
print(maior_inserido(num1, num2))
