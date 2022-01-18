"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}
"""
# Exemplos

numeros = {num for num in range(1, 8)}
print(numeros)

#  Outro exemplo
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Desafio! Faça uma alteração na estrutura acima para gerar um dicionário ao invez de set
numeros = {x: x ** 2 for x in range(10)}
print(numeros)
