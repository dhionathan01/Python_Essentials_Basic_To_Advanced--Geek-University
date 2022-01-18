"""
Generators Expression

Em aulas anteriores nós estudamos:
- List Comrehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension... Porque elas se chamam Generators

Quando vimos all e any utilizamos o seguinte exemplo:

nomes = ['Carlos', 'Camila', 'Carla', 'Cassino', 'Cristina', 'Daniel']
print(any([nome[0] == 'C' for nome in nomes]))
Em Generators podemos fazer de uma forma diferente
"""
'''
nomes = ['Carlos', 'Camila', 'Carla', 'Cassino', 'Cristina', 'Daniel']
print(any(nome[0] == 'C' for nome in nomes))
"""
OBS: O Generators assim como o map e o filter ele se ao destroe após o seu uso e retorna um objeto ou seja um
generato object para poder fazer seu uso é necessário que ele seja convertido para alguma coleção (list, tuple...).
"""

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator obs: Generator ocupa menos recurso de memória.
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)
'''

# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória de elemento passado como parâmetro
from sys import getsizeof
'''
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(92345668823))

print(getsizeof(True))
'''

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Compreension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa em memória')
print(f' List Comprehension: {list_comp} Bytes')
print(f' Set Comprehension: {set_comp} Bytes')
print(f' Dictionary Comprehension: {dic_comp} Bytes')
print(f' Generator Expression: {gen} Bytes')
'''
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
'''