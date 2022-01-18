"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem básicamente duas diferneças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla.

"""

'''
# CUIDADO 1: As tuplas são repretsentadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6,)
print(tupla1)
print(type(tupla1))

# Observe que abaixo também se trata de uma tupla porém não há presença de parênteses, somente do separador (vírgula).

tupla2 = 1, 2, 3, 4, 5, 6,
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento.

tupla3 = (4)    # Isso NÃO é uma tupla.
print(tupla3)
print(type(tupla3))

tupla4 = (4,)   # Isso é uma tupla.
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso de parênteses.
'''
'''
# Assim como na lista, podemos gerar uma tupla de forma dinámica com o range (início, fim, passo)

tupla = tuple(range(11))
print(tupla)
'''
'''
# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla

print(escola)
print(curso)
# OBS: Caso não haja variáveis suficiente para receber todos os índices da tupla, ocorre erro.
# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.
'''
'''
# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho.
# * Se os valores forem todos inteiros ou reais.

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
'''
'''
# Concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)
print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2    # Tuplas são imutáveis

print(tupla3)
print(tupla1)
print(tupla2)

# Forma de alterar uma tupla
tupla1 = tupla1 + tupla2    # Tuplas são imutáveis, mas podem ser sobrescitas, ela não é uma constante.
print(tupla1)
'''
'''
# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)
'''
'''
# Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
'''
'''
# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))

user = tuple('Dhionathan Lanzoni Jobim')
print(user)
print(user.count('a'))
'''
# Dicas na utilização de tuplas

# Devemos utilziar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1 (Não tem motivo, nem lógica modificar uma lista que contenha os meses do ano)

meses = ('Janeiro', 'Fevereiro', 'Março',
         'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro',
         'Outubro', 'Novembro', 'Dezembro')
'''
# O acesso a elementos de uma tupla também é semelhante a de uma lista.
print(meses[5])     # Exiba o que está contido no índice 5 da tupla

# Iterando com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1
'''
'''
# Verificamos em qual índice um elemento está na tupla
print(meses.index('Fevereiro'))
# OBS: Caso o elemento não exista, será gerado ValueError.

# Porque usar Tuplas ?
# 1 - Tuplas são mais rápidas.
# 2 -  Tuplas deixam seu código mais seguro. Devido ao fato de que trabalhar com dados imutáveis, trazem segurança.
'''
# Copiando tuplas.
# Forma 1
tupla = (1, 2, 3, 4, 5)

nova = tupla     # Tuplas não tem problema com Shallow Copy.
print(nova)

# Forma 2

outra = (6, 7, 8, 9)

nova = nova + outra
print(nova)
