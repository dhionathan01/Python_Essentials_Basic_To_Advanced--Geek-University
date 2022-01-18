"""
Tipo Float

Tipo real, decimal

Casas decimais
OBS: O separador de casas decimais na programçaõ é o ponto e não a vírgula
"""

# Float do metodo errado
valor = 1, 44  # -> Isso é um dado tipo Tupla, não float.
print(valor)
print(type(valor))

# Correto
valor = 1.44
print(valor)
print(type(valor))

# A vírgula pode ser usada para atribuição de Duas variáveis:
valor1, valor2 = 1, 44  # -> Tipos inteiro
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um flaot para int obs variável "valor" que foi declarada como valor = 1.44, na linha 16
"""
OBS: Ao converter valores float para inteiros se perde a precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
