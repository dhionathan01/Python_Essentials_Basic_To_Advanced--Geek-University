"""
Utilizando Lambdas

Conhecidas por  Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções anônimas.

# Função em Python


"""

'''
# Funçao em Python


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))
'''

'''
# Exepressão Lambda
# lambda x: 3 * x + 1

# Como utilizar a expressão lambda ?

calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

'''

'''
# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(' angelina   ', ' JOLIE  ')
print(nome_completo(' angelina   ', ' JOLIE  '))
print(' FELICITY          ', '  jones   ')
print(nome_completo(' FELICITY          ', '  jones   '))

# Em funções Python podemos ter nenhuma ou varias entradas. em Lambdas também

amar = lambda: 'Como não amar Python ?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y,  z: 3 / (1 / x + 1 / y + 1/ z)

# n = lambda x1, x1, ..., xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumento do que parâmetros esperados teremos TypeError
'''

# Outro exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G Wells', 'Leigh Backett']
print(autores)
# Fazendo ordenação por sobrenome

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# Função quadratica
# f(x) = a * x ** 2 + b * x + c

# Definindo a função


def geradora_funcao_quadratica(a, b, c,):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)


print(teste(0))
print(teste(1))
print(teste(2))


print(geradora_funcao_quadratica(3, 0, 1)(2))


