"""
Listas

Listas em Python fucionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também podermos colocar QUALQUER tipo de dado.
Por exemplo nas Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dadao fixo:
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5,
    este array será sempre do tipo inteiro e poderá ter sempre no máximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo, Ou seja, podemos colocar qualquer tipo de dado (int, float...)
As listas em Python são representadas por colchetes: []

Listas são mutáveis: Ou seja elas podem mudar constantemente.
"""
type([])
lista1 = [1, 23, 12, 3, 14, 54, 1, 99, 23, 87, 30, 23, 21, 1, 90, 105, 3, 143, 111]

lista2 = ['D', 'h', 'i', 'o', 'n', 'a', 't', 'h', 'a', 'n', '', 'J', 'o', 'b', 'i', 'm']

lista3 = []

lista4 = list(range(11))  # Criando uma lista de 0 a 11

lista5 = list('Dhionathan Jobim')
# print(lista5)
"""
Repare que a lista 5 é exibida da mesma forma que a lista2, isso se dá ao fato do Python entender
toda a letra como uma string, não havendo diferença entre char e string.
"""
# Podemos facilmente checar se determinado valor está contido na lista.
"""
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')
"""
# Podemos facilmente ordenar uma lista, observe a lista1 definina anteriormente, se encontra fora de ordem.
'''
print(lista1)
lista1.sort()
print(f'Lista 1 ordenada \n {lista1}')

# Também é possivel fazer isso  com nomes, para que sejam ordenados de forma alfabética.
lista6 = ['Dhionathan', 'Ana Maria', 'Carlos']
lista6.sort()
print(lista6)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista.
print(lista1.count(1))
print(lista5.count('a'))
'''
"""
Para adicionar elementos em listas, utilizamos a função append.
"""
'''
print(lista1)
lista1.append(500)
print(lista1)

# OBS: Com append, só conseguimos adicionar 1 elemento por vez.
# lista1.append(12, 34, 56) # Erro
# A maneira que temos de adicionar mais de 1 elemento por vez é por meio do elemento extend.
lista1.extend([123, 144, 133, 122, 133])
print(lista1)
# Repare que ao fazer isso com o append, ele adicionara uma nova lista, e não acrescentar somente os números
# como acontece no extend, porém o extend também não aceita valor único.
lista1.append([331, 221, 441, 121, 221])
print(lista1)
'''
"""
Podemos observar que tanto o append, quanto o extend adicionam os valores ou números sempre no final indo
da esquerda pra direita, podemos inserir um novo elemento na posição desejada informando a posição do índice
por meio do comando insert. Isso não vai substituir o valor inicial, o mesmo será descolado para a direita da lista,
ocupando o índice seguinte.
EX:
"""
'''
print(lista1)
lista1.insert(2, 'Ocupando Indice 2')
print(lista1)

# Podemos facilmente juntar duas lista.
lista6 = lista1 + lista2  # Criando uma nova lista, que conterá as duas.
print(lista6)
lista1.extend(lista2)  # Adicionando a lista 2 diretanamente na 1 por meio do extend.
print(lista1)
'''
'''
Descomente para testar
lista1 = lista1 + lista2  # Ou por meio da concatenação da própria lista, recebendo ela mesma mais a outra;
print(lista1)
'''
# Inverter uma lista.
# Forma 01:
'''
print(lista1)
print(lista1.reverse())
# Forma 02:
print(lista2)
print(lista2[::-1])
'''
'''
# Copiar uma lista.
lista2_copia = lista2.copy()
print(lista2_copia)
'''
'''
# Calculando o tamanho de uma lista.
print(lista2)
print(len(lista2))
'''
'''
# Removendo o último elemento de uma lista.
# OBS: Não somente remove o último elemento mas também o retorna.
print(lista2)
lista2.pop()
print(lista2)

# Podemos remover um elemento pelo índice
# OBS: Os elementos á direita do índice serão deslocados para a esquerda, fazendo com que não tenha um índice vazio.
print(lista2)
lista2.pop(2)
print(lista2)

# Deletando todos os elementos de uma lista (zerando a lista):
print(lista2)
lista2.clear()
print(lista2)
'''
'''
# Replicar elementos em uma lista:
lista6 = [10, 21, 32, 43, 54, 65]
print(lista6)
lista6 = lista6 * 3
print(lista6)
lista6.pop()
print(lista6)
'''
'''
# Converter string para lista.
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)
# OBS: Por padrão, o Split, separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')  # Especificando que o separador da lista é  vírgula.
print(curso)
'''
'''
# Convertendo lista para string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)
# Abaixo estamos falando: Pega a lista6, coloca um espaço entre cada elemento e transforma em uma string.
curso = ' '.join(lista6)
print(curso)
# Abaixo estamos falando: Pega a lista6, coloca um $ entre cada elemento e transforma em uma string.
curso = '$'.join(lista6)
print(curso)
'''
'''
# Podemos colocar qualquer tipo de dado dentro de uma lista ex:
lista_all = [10, 'dhionathan', True, -10, 1.23, 5434343, [10, 23, 121, 314]]
print(lista_all)
'''
'''
# Para cada elemento na lista1, imprima o elemento.
for elemento in lista1:
    print(elemento)
'''
# Iterando Listas
'''
# Exemplo com FOR:
# Somar todos os elementos dentro de uma lista
lista07 = [20, 30, 53, 21, 66, 34, 22.5, 65.3, 21.8, 21.3, 67.7]
print(lista07)
soma = 0
for elemento in lista07:
    soma = soma + elemento
print(f'Resultado da soma dos elementos: {soma}')

#  É possível também concatenar strings da mesma maneira, BASTA MUDAR O TIPO DE DADO EM SOMA.
lista08 = ['D', 'H', 'I', 'O', 'J', 'O', 'B', 'I', 'M']
print(lista08)
soma = ''
for elemento in lista08:
    soma = soma + elemento
print(f'Resultado da soma dos elementos: {soma}')
'''
'''
# Exemplo 2 -  Utilizando While.
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para finalizar : ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
'''
'''
# Utilizando variáveis em listas.
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros_teste = [num1, num2, num3, num4, num5]
print(numeros_teste)
'''
'''
# Fazemos acesso aos elementos de forma indexada.

#            0        1         2         3          4
cores = ['Azul', 'Amarelo', 'Branco', 'Verde', 'Vermelho']

print(cores[0])  # Azul.
print(cores[1])  # Amarelo.
print(cores[2])  # Branco.
print(cores[3])  # Verde.
print(cores[4])  # Vermelho.
"""
- Exibindo de forma invertida. Explicação Aula 32. Listas 01:28:30 (Hora/ minuto/ segundo).
  Para melhor entendimento do índice negativo pense que na lista como um círculo, onde
o final de um elemento está ligado ao ínicio da lista.
"""
print(cores[-1])  # Vermelho.
print(cores[-2])  # Verde.
print(cores[-3])  # Branco.
print(cores[-4])  # Amarelo.
print(cores[-5])  # Azul.
# print(cores[-6])  # Erro, pois não existe indice -6
'''
'''
cores = ['Azul', 'Amarelo', 'Branco', 'Verde', 'Vermelho']
# Loops com Len
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Gerando uma lista com indices e elemento
print(cores)
cores = list(enumerate(cores))
print(cores)
'''
'''
# OBS: Lista aceitam valores repetidos:
lista01 = []
lista01.append(12)
lista01.append(23)
lista01.append(31)
lista01.append(12)
lista01.append(23)
print(lista01)
'''
'''
# Outros métodos não tão importantes também úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice na lista está o valor 6 ?
# print(numeros.index(6))
# Testando :
x = int(input('Qual o valor deseja saber o indice ? '))
print(numeros.index(x))
# OBS: Caso não tenha o elemento na lista, era ocorrer um erro.
# OBS: Caso tenha mais de um elemento igual, ele retornara o índice do primeiro elemento encontrado

# Podemos fazer buscas dentro de um range, ou seja a partir de qual índice começar a buscar.
print(numeros.index(5, 1))  # Buscando o número 5 a partir do índice 1
print(numeros.index(5, 2))  # Buscando o número 5 a partir do índice 2
# OBS: Caso não tenha o elemento na lista, era ocorrer um erro.

# Podemos fazer busca dentro de um range inicio/fim
print(numeros.index(8, 3, 6)) # Buscando o número 8 a partir do indice 3 a 6.
'''

'''
# Revisão de slicing

# lista[inicio:fim:passo]
# range (inicio:fim:passo)

# Trabalhando com slice de lista com parâmetro 'inicio'


lista = [1, 2, 3, 4]

print(lista[1:])    # Iniciando no Índice 1 e pegando todos os elementos restantes.

# Trabalhando com slice de lista com o parametro 'fim' .

print(lista[:2])    # Começa no índice 0, pega até o indíce 1 OBS: (2 - 1).

print(lista[:4])    # começa em 0, pega até o indice 3 OBS: (4 - 1).

print(lista[1:3])   # começa no índice 1 vai até o índice 2 (3 - 1).


# Trabalhando com slice de lista com o parâmetro 'passo' .

print(lista[1:4:2])  # Começa no índice 1 vai até o índice 3 ( 4 - 1) de 2 em 2.

print(lista[1::2])  # Começa em 1, vai até o final, de 2 em 2.

print(lista[::2])   # Começa em 0, vai até o final, de 2 em 2.
'''
'''
# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho .

# Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(lista))   # soma
print(max(lista))   # máximo valor
print(min(lista))   # mínimo valor
print(len(lista))   # tamanho da lista ( Quantos índices foram preechidos)
'''

'''
# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
'''

'''
# Desempacotamento de listas
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
print(lista)
# OBS: Caso não haja variáveis suficiente para receber todos os índices da lista, ocorre erro.
'''
'''
# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)
nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja modificando uma lista, não afeta a outra. Isso em Python
# é chamado de Deep Copy (cópia profunda)

'''
'''
# Forma 2 Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista

print(nova)
nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas após realizar
# modificação em uma das listas, essa moidificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.
'''