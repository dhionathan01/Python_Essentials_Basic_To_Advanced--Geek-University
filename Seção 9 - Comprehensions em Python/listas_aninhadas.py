"""
Listas Aninhadas (Nested Lists)
 - Algumas linguagens de programação (C/Java) Possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as listas
Que no caso foge das duas limitações básicas das outras linguagens que são o número
de possições e a timpagem ja´que se vc criar um vetor de tipo inteiro vc n pode colocar outro tipo de valor dentro
dela.
numeros  = [1, b, 3.234, True, 5]

"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print(listas)
'''
# Como fazemos para acessar os dados ?

print(listas[0][1])  # 2
print(listas[2][1])  # 8
'''

'''
# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)
'''

'''
# List comprehension

[[print(valor) for valor in lista] for lista in listas]
'''
# Outros Exemplos gerando um tabuleiro/matrix 3x3

# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando Jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)
