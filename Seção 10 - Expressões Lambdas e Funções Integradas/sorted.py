"""
Sorted

OBS: Não confunda, apesar do nome, com  a função sort() que já estudamos em Listas. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.
"""

# Exemplos
'''
numeros = (6, 1, 8, 2)
print(numeros)
print(sorted(numeros))  # Ordenar do menor para o maior
print(numeros)
""" 
    OBS: Observe que ao printar o valor novamente a tupla volta  a seu estado original ou seja, o sorted gera uma nova
lista alterando seu resultado e conserva a original, diferente do .sort() que altera a lista original em si.
    OBS - 2: O sorted SEMPRE retorna uma lista com os elementos do iterável ordenados.
"""
numeros = [6, 1, 8, 2]
#   Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True))    # Ordena do maior para o menor

# Sabemos que o sorted sempre retorna uma lista porém podemos fazer a conversão da lista para outro tipo de dado
print(tuple(sorted(numeros)))   # Convertendo resultado do sorted para Tupla
'''

#   Podemos Utilziar o Sorted() para coisas mais complexas.

'''
usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': [], 'cor': 'amarelo'},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'vou sair hoje']},
    {'username': 'gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'},
]

print(usuarios)
# print(sorted(usuarios, key=len, reverse=True))
print(sorted(usuarios, key=lambda usuario: usuario["username"]))    # Ordenando pelo usuário (alfabética)
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))     # Ordenando pelo número de tweets
'''

# Último exemplo

musicas = [
    {'titulo': "Thunderstruck", 'tocou': 3},
    {'titulo': "Dead Skin Mask", 'tocou': 2},
    {'titulo': "Back in Black", 'tocou': 4},
    {'titulo': "Too old to rock'in' roll, to young to die", 'tocou': 32}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
# Ordena das mais tocadas para as menos tocadas
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
