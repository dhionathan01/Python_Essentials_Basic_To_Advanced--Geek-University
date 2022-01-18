"""
Módulo Collections - Named Tuple
# Recap tupla
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São tuplas, diferenciadas, onde especifcamos um nome para a mesma a também parâmetros.
"""
from collections import namedtuple

#   Precisamos definir o nome e parâmetros

#   Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

#   Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

#   Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

# Forma 1

print(ray)
print(ray[0])   # idade
print(ray[1])   # raça
print(ray[2])   # nome
print(ray[1:])  # raça ~ nome

# Forma 2

print(ray.idade)    # idade
print(ray.raca)     # raça
print(ray.nome)     # nome
