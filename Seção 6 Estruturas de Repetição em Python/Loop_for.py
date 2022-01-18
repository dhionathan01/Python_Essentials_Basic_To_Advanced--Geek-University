"""
Loop For

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

Sintaxe do for em C ou Java

for(int i = 0; i < 10; i++){
    \\execução do loop
}

Sintaxe for em Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Dhionathan Jobim'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""
'''
nome = 'Dhionathan Jobim'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)
for i in nome:
    print(i)
# Exemplo de for 2 (Iterando sobre uma lista)
for i in lista:
    print(i)
# Exemplo de for 3 (Iterando sobre um range)
'''
"""
range(valor_inicial, valor_final)
OBS: o valor final não é incluído.
range(1, 10):
1
2
3
4
5
6
7
8
9
10 - Não é incluido ou contado
"""
'''
for i in range(1, 10):
    print(i)
'''
"""
nome = 'Dhionathan Jobim'
Enumerate:
((0, 'D'), (0, 'h'), (0, 'i'), (0, 'o'), (0, 'n'), (0, 'a'), (0, 't'), (0, 'h'), (0, 'a'), (0, 'n') ...)
"""
'''
for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
'''
'''
nome = 'Dhionathan Jobim'
for valor in enumerate(nome):
    print(valor)  # Funcionamento do enumerate
'''
'''
qtd = int(input('Quantas vezes deseja rodar o loop? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}°/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')
'''
'''
nome = 'Dhionathan Jobim'
for letra in nome:
    print(letra, end='') # imprimir print sem quebra de linha automática
'''
# Usando emoticons / emoji

# Original: U+1F60D -> Código Unicode link: https://apps.timwhitlock.info/emoji/tables/unicode
# Modificado: U0001F60D -> Código convertido para o uso em Python
emoji_apaixonado = '\U0001F60D'
for num in range(1, 11):
    print(emoji_apaixonado * num)
