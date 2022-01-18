"""
Leia um Número fornecedio pelo usuário. Caso esse número seja positivo, calcule a raiz quadrada do número.
Se negativo, mostre uma mensagem dizendo que o número é inválido.
"""
valor = float(input('Insira o valor que deseja saber a raiz quadrada: '))
if valor >= 0:
    raiz = valor ** 0.5
    print(f'A raiz quadrada de {valor} é igual a {raiz}\n Raiz reduzida: {raiz:.2f}')
else:
    print('O valor informado é inválido')

