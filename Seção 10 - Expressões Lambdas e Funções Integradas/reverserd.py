"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas.

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.

A função reverserd() retorna um iterável chamado List Reverse Iterator
"""

# Exemplos
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, Tupla ou Conjunto
# Lista
print(list(reversed(lista)))
# Tupla
print(tuple(reversed(lista)))
# Set Obs: Em conjuntos não é possível definir a ordem dos elementos
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

# Podemos fazer o mesmo sem o uso do for
print('\n')
print(''.join(list(reversed('Dhionathan Jobim'))))

# Já vimos como fazer isso mais fácil com o slice de strings
print('Dhionathan Jobim' [::-1])

# Podemos também utilizar o reversed para fazer um loop for reverso

for n in reversed(range(0, 10)):
    print(n)

# Apesar que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)
