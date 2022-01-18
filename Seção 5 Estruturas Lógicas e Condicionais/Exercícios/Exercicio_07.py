"""
Faça um progrma que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima mensagem
números iguais
"""
numero1 = float(input('Insira o primeiro número: '))
numero2 = float(input('Insira o segundo número: '))

if numero1 > numero2:
    print(f'O Primeiro número "{numero1}" é maior que o segundo número "{numero2}"')
elif numero2 > numero1:
    print(f'O Segundo número "{numero2}" é maior que o primeiro número "{numero1}"')
elif numero1 == numero2:
    print('Números iguais.')

