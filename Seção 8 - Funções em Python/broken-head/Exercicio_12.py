"""
Escreva uma função que receba um número inteiro maior do que zeo e retorne a soma de todos os seus algarismos.
por exemplo ao número 251 corresponderá o valor 8 (2 + 5 +1).
Se o número lido não for maior do que zero, o programa terminará com a mensagem "número inválido".
"""


def soma_algorismo(num):
    num = list(num)
    convert_to_int = []
    for valor in num:
        convert_to_int.append(int(valor))
    return sum(convert_to_int)


numero = input('Informe o Número: ')
print(f'Soma de cada caracter informado: {soma_algorismo(numero)}')
