"""
Funções com retorno

numeros = [1, 2, 3]
numeros.pop()

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')
ret_pr = print(numeros)
print(f'Retorno de print: {ret_pr}')
"""

# Exemplo função

'''
def quadrado_de_7():
    print(7 * 7)
"""
Observe abaixo que que embora seja exibido o valor 49, ele não é retornando, ele apenas cumpre a função print e exibe
o resultado da operação 7 * 7, porém ao definir uma variável para o receber e exibir oq foi retornado, retorna 'none'
OBS: Quando nenhum valor é retornado, o retorno é tido como none.
"""

ret = quadrado_de_7()


print(f'Retorno: {ret}')
'''

# Vamos refatorar está função para que ela retorne o valor:
# OBS: Funções em Python que retornam valores, devem retornar estes valores com a palavra reservada return

'''
def quadrado_de_7():
    return 7 * 7    # Definindo Retorno da função
'''

'''
ret = quadrado_de_7()
# OBS que a função ret agora recebe o retorno da operação 7 * 7.
print(f'Retorno {ret}')
'''
# Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução
# para outras funções
'''
print(f' Retorno: {quadrado_de_7()}')
'''
# Refatorando a primeira função:

'''
def diz_oi():
    return 'Oi '


alguem = 'Dhionathan'

print(f'{diz_oi()+alguem}')
'''

"""
OBS: Sobre a palavra reservada return
1 - Ela Finaliza a função, ou seja, ela sai da execução da função.
2 - Podemos ter, em uma função diferentes returns.
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores.
"""

# Exemplos 1 Ela Finaliza a função, ou seja, ela sai da execução da função.

'''


def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi!'
    print('Estou sendo executado após o retorno')
    """" Como o return encerra a função repare que a linha acima n vai ser impressa """


print(diz_oi())
'''

'''
# Exemplo 2 Podemos ter, em uma função diferentes returns.


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())
'''

# Exemplo 3 Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores

'''
def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

# OBS Podemos exibir sem fazer o desempacotamento do retorno porém o python entendera o retorno como uma tupla, Observe:
print('Retorno sem Desempacotar')
print(outra_funcao())
print(type(outra_funcao()))
'''

from random import random


def joga_moeda():
    # Gera um número pseudo - Randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
