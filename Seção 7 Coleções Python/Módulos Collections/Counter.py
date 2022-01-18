"""
Módulo Collections - Counter (Contador)

Collections -> High-performace Container Date types ( Tipos de dados de container de alta performace).

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências
desse elemento.
"""

# Realizando o import
'''
from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 45, 45, 66, 43, 34]

# Utilizando o Counter

res = Counter(lista)

print(type(res))

print(res)
# Counter({5: 7, 6: 4, 1: 3, 3: 3, 4: 3, 2: 2, 45: 2, 66: 1, 43: 1, 34: 1})
# Veja que, para cada elemeto da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências
'''

'''
# Exemplo 2
from collections import Counter

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
'''

from collections import Counter

# Exemplo 3
texto = """A Wikipédia é um projeto de enciclopédia multilíngue de licença livre,[5][6] baseado na web e escrito de
    maneira colaborativa.[6] O projeto encontra-se sob administração da Fundação Wikimedia,[7] uma organização sem fins
    lucrativos cuja missão é "empoderar e engajar pessoas pelo mundo para coletar e desenvolver conteúdo educacional sob
    uma licença livre ou no domínio público, e para disseminá-lo efetivamente e globalmente"."""
palavras = texto.split()
# print(palavras)
res = Counter(palavras)
print(res)
# Ecnontrando as 5 plavras com mais ocorrências no texto
print(res.most_common(5))
