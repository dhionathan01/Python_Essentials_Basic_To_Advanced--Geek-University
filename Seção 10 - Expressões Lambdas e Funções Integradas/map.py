"""
Map

Com map, fazemos mapeamento de Valores para função.
"""
'''
import math


def area(r):
    """Calcula a área de um círculo com raio 'r'."""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))
print(areas)

# Forma 2 - Map
# map é uma função que recebe dois parâmetros: O primeiro a função o segundo um iterável

areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))  # Covertendo objeto mapa para lista, para poder ser exibido.

# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilziar a função map dps da primeira utilização do resultado ele zera.
'''

# Para fixar - Map

# Temos dados iteraveis :

# Dados : a1, a2, ..., an

# Temos uma função:

# Função:

# Função: f(x)

# Utilizamos a função map(f, dados) onde  map irá 'mapear' cada elemnto dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), f(...), f(an)

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

print(cidades)
# Convertendo graus C para Fareheint fórmula : (f = 9/5 * c + 32)

# Lambda

convertendo_graus = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(convertendo_graus, cidades)))

