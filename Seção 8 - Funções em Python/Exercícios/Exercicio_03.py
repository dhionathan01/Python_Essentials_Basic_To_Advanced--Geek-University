"""
Faça uma função para verificar se um número é positivo ou negativO.
Sendo o valor de retorno 1 se positvo, -1 se negativo.
"""


def validar_numero(valor):
    if valor > 0:
        return 1
    elif valor == 0:
        return 0
    else:
        return -1


num = int(input('Insira um número: '))
print(validar_numero(num))
