"""
Faça um Programa que Leia um número e, caso ele seja positivo, calcule e mostre:

- O número digitado ao quadrado.
- A raiz quadrada do número digitado
"""

numero = float(input('Insira um valor Positivo: '))
if numero >= 0:
    raiz = numero ** 0.5
    print(f'A raiz quadrada de {numero} é igual a {raiz}')
    print(f'Valor da Raiz reduzida: {raiz:.2f}')
    quadrado = numero ** 2
    print(f'O quadrado de {numero} é igual a {quadrado}')
    print(f'Valor do Quadrado Reduzido {quadrado:.2f}')

else:
    print('Número inserido é inválido')
