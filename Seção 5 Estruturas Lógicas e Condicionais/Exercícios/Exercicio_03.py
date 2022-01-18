"""
Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o numero ao quadrado.
"""

numero = float(input('Insira um valor : '))
if numero >= 0:
    raiz = numero ** 0.5
    print(f'A raiz quadrada de {numero} é igual a {raiz}')
    print(f'Raiz Reduzida: {raiz:.2f}')

else:
    quadrado = numero ** 2
    print(f'O quadrado de {numero} é igual a {quadrado}')
