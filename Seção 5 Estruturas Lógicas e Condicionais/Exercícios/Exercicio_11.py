"""
Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos.
Por exemplo, ao número 251 correspondera o valor 8 (2+5+1). Se o número lido não for maior do que zero, o programa
terminará com a mensagem "Número inválido".
"""

numero = int(input('Insira um número inteiro : '))

if numero > 0:
    numero = str(numero)
    total = 0
    for i in range(len(numero)):
        total = total + int(numero[i])
    print(f'Soma: {total}')

else:
    print('Número inserido Inválido')


