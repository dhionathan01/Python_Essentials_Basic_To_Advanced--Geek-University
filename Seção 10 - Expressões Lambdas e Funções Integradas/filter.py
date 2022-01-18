"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.
"""

#   Biblioteca para trabalhar com dados estatísticos
import statistics
'''
#   Dados Coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média: {media}')
# OBS: Assim como a função map(),a filter() recebe dois parâmetros, sendo uma função e um iterável

# Criamos uma lambda 'x' que captura o argumento 'dados' de forma iterável e verifica se dados é maior que a media.
res = filter(lambda x: x > media, dados)
print(list(res))
# OBS: Assim como na função map() após serem utilizados os dados de filter() eles são exclídos da memória
print(f'Novamente: {list(res)}')
'''

'''
# Removendo campos vazios com filter

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)

res = filter(None, paises)
print(list(res))
'''

'''
# Métodos alternativo s
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
# Faça um filtro onde o len do pais for maior que zero
# res = filter(lambda pais: len(paises) > 0, paises)
res = filter(lambda pais: pais != '', paises)
print(list(res))
'''

"""
A diferença entre map () e filter() é:

 - map() -> Recebe dois parâmetro, uma função e um iterável e retorna um objeto mapeandoa a função para cada elemento
 do iteravel.
 
 - filter() Recebe dois parametros, uma função e um iterável e ternoa um objeto filtrando apenas os elementos de acordo
 com com a função
 
"""
'''
# Exemplo mais complexo

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'vou sair hoje']},
    {'username': 'gal', 'tweets': []},
]
print(usuarios)

# Filtrar os usuários que estão inativos no Twitter

# Forma 1
# inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda user: not user['tweets'] == 0, usuarios))

print(inativos)
'''

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua Instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
