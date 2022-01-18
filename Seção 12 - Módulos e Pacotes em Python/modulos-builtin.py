"""
Trabalhando com Módulso Builtin (Módulos ingetrados, que já vem instalados no Python)
________________________
|Python|Módulos builtin|
-----------------------
Esses módulos já estão instalados mas não prontos para uso,para fazer seu uso é preciso efetuar um import.
https://docs.python.org/3.7/py-modindex.html
"""
'''
# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())
'''
'''
# Podemos importar todas as funções de um módulo utilizando o *
from random import *
# OBS: Fazendo o import dessa forma não é preciso chamar a biblioteca e depois a função 'print(random.random())'
# Basta chamar somente a função como abaixo:
print(random())
'''
'''
# Utilizando alias (apelidos) para funções
from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())
'''
# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import (
                    random,
                    randint,
                    shuffle,
                    choice
                    )

print(random())
print(randint(3, 7))
lista = ['Dhionathan', 'Jobim', 'Python', 'Essentials']
shuffle(lista)
print(lista)
print(choice('Dhionathan'))
