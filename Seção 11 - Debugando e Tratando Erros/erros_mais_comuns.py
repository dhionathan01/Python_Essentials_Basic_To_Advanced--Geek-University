"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python não
reconhece como parte da linguagem
"""

# 1 - Exemplos SyntaxError
# Exemplo 1:
'''
def funcao:
    print('Dhionathan Jobim')
'''
"""
Sabemos que uma função se dá pela abertura e fechamento de parêntese em sua definição, a forma correta seria
def funcao():
    print('Dhionathan Jobim')
"""

# Exemplo 2
'''
None = 1
'''
"""
Sabemos que None é uma palavra reservada do sistema, logo ela não poder ser usada como variável e nem ter um
valor atribuído a ela.
"""

# Exemplo 3
'''
return
'''
"""
Sabemos que return é uma palavra reservada geralmente utilizada dentro de uma função que possui o return
"""
# 2 - Exemplo NameError -> Ocrre quando uma virável ou função não foi definida.

# Exemplo 1
'''
print(geek)
'''

# Exemplo 2
'''
geek()
'''
# Exemplo 3
'''
a = 18
if a < 10:
    msg = 'É menor que 10'
print(msg)
'''

# 3 - TypeError -> Ocorre quando uma Função/Operaçao/Ação é aplicada a um tipo errado.

# Exemplo 1
'''
print(len(5))
'''
# Exemplo 2
'''
print('Geek' + [])
'''

"""
4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido.
"""
# Exemplo 1 / 2
'''
lista = ['Geek']
print(lista[2])     # 1
print(lista[0][10])     # 2
'''
"""
5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto
mais o valor inapropriado
"""
# Exemplo 1
'''
print(int('Geek'))
'''

# 6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

# Exemplos KeyError
'''
dic = {'python': 'univerity'}
print(dic['geek'])
'''

# 7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

# Exemplo 1
'''
tupla = [11, 2, 31, 4]
print(tupla.sort)
'''

# 8 - IdentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

# Exemplo 1
'''

def nova():
print('Dhionathan')


nova()
'''

# Exemplo 2
'''
for i in range(10):
i+1

print(i)

OBS:
* Exceptions e Erros são sinônimos na programação.
* Importante ler e prestar atenção na saída de erro.
'''