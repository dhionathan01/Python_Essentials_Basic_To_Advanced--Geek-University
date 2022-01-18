"""
Escreva o menu de opções abaixo. Leia a Opção do usuário e execute a operação escolhida. Escreva uma mensagem de erros
se a opção for inválida.
1 - Soma de 2 números.
2 -  Diferença entre 2 números (maior pelo menor)
3 - Produtos entre 2 números
4 - Divisão entre 2 números (O denominador não pode ser zero).
"""
print('Escolha uma das opções. \n'
      '1 - Soma de 2 números. \n'
      '2 - Diferença entre 2 números(maior pelo menor). \n'
      '3 - Produto entre 2 números. \n'
      '4 - Divisão entre 2 números (o denominador não pode ser zero). ')
option = int(input('Opção: '))

if option == 1:
    valor1 = float(input('Insira o valor 1: '))
    valor2 = float(input('Insira o valor 2: '))
    total = valor1 + valor2
    print(f'{valor1} + {valor2} = {total}')
elif option == 2:
    valor1 = float(input('Insira o valor 1: '))
    valor2 = float(input('Insira o valor 2: '))
    total = valor1 - valor2
    print(f'{valor1} - {valor2} = {total}')
elif option == 3:
    valor1 = float(input('Insira o valor 1: '))
    valor2 = float(input('Insira o valor 2: '))
    total = valor1 * valor2
    print(f'{valor1} * {valor2} = {total}')
elif option == 4:
    valor1 = float(input('Insira o valor 1: '))
    valor2 = float(input('Insira o valor 2: '))
    if valor2 != 0:
        total = valor1 / valor2
        print(f'{valor1}/{valor2} = {total}')
    else:
        print('Não é possível realizar divisão com denominador 0')
else:
    print('Opção Inválida')

