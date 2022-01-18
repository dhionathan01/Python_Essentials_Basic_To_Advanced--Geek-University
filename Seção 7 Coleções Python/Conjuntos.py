"""
Conjuntos

- Conjuntos em qualquer linguagem de progração, estamos fazendo referência à teoria dos conjuntos
da Matemática.

- No Python, os conjuntos são chamados de Sets. Da mesma forma que na matemática:
- Sets (conjuntos) Não possuem valores duplicados:
- Sets ( Conjuntos) Não possuem valore ordenados:
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles.
Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

Os conjutos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
    - Um Dicionário tem chave/valor.
    - Um Conjunto tem apenas valor.
"""

# Definindo um conjunto:
'''
# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado
# sem gerar erro e não sera incluido no conjunto.
'''
'''
# Forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')
'''

'''
# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} Número de Elementos: {len(lista)}')

# Tuplas aceitam valores duplicados, então temos 10 elementos.
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} Número de Elementos: {len(tupla)}')

# Dicionários não aceitam chaves duplicadas, as chaves são ignoradas e temos 8 elementos.
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} Número de Elementos {len(dicionario)}')

# Conjuntos não aceitam chaves duplicadas, as chaves são ignoradas e temos 8 elementos.
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} Número de elementos: {len(conjunto)}')
'''

'''
# Assim como quase tudo em Python podemos colocar vários tipos de de dados misturados em sets.

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))
# Podemos iterar em um set normalmente
for valor in s:
    print(valor)
'''
'''
# Usos interesantes com sets (Conjuntos)

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas temos nessa lista.

# Podemos utilziar o set para isso:
print(set(cidades))
print(len(set(cidades)))
'''

'''
# Adicionando elementos em um conjunto

s = {1, 2, 3}
print(s)
s.add(4)  # Adicionando o elemento 4 ao conjunto.
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(s)
'''
'''
# Remover elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)  # Lembresse que o conjunto não é indexado, ou seja informamos o valor a ser removido, não o índice.
print(s)
# OBS 1: Caso o valor não seja encontrado será gerado o erro "KeyError".
# OBS 2: Nenhum valor é retornado

# Forma 2
print(s)
s.discard(2)
print(s)

# OBS: Se o valor não for encontrado nenhum erro é gerado.
'''

'''
# Copiando um conjunto para outro...

# Forma 1 - Deep Copy
s = {1, 2, 3}
novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)
'''

'''
# Forma 2 - Shallow Copy
s = {1, 2, 3}
novo = s

novo.add(4)
print(novo)
print(s)
'''
'''
# Podemos remover todos os itens de um conjunto
s = {1, 2, 3}
s.clear()
print(s)
'''
'''
# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso de Python e o outro com estudadntes de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
# Veja que alguns alunso estudam Python e Java, logo temos valores repetidos.

# Precisamos gera rum conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

# unicos1 = estudantes_python.union(estudantes_java)
# print(unicos1)
# {'Fernando', 'Gustavo', 'Guilherme', 'Julia', 'Pedro', 'Ellen', 'Marcos', 'Patricia', 'Ana'}
unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)
# {'Pedro', 'Patricia', 'Gustavo', 'Ellen', 'Marcos', 'Fernando', 'Guilherme', 'Julia', 'Ana'}
'''
'''
# Forma 2 - Utilizando caracter Pipe | 
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
unicos2 = estudantes_java | estudantes_python
'''
'''
# Gerar um conjunto de estudantes que estão em ambos os cursos:

# Forma 1 - utilizando intersection
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)
'''
'''
# Gerar estudantes que não estão no outro curso ( utiliznado difference 'Diferente')

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
'''

# *Soma, *Valor Máximo, *Valor Mínimo, Tamanho

# * Se os valores forem todos inteiros ou reais.

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
