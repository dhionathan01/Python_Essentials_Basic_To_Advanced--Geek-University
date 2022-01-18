"""
Loop While

Forma geral

while expressão_booleana:
    //execução do loop

o bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expresão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num < 5 # False

Exemplo prático:
"""
'''
numero = 0
# Enquanto numero < 10 Faça
while numero < 10:  # Para entrar no loop a variável passar por uma verificação, se True, o loop é excutado.
    print(numero)
    numero = numero + 1  # Caso não tiver um contador ou forma de tornar a variável false, o Loop é infinito.
'''
# Exemplo 02:
resposta = ''
while resposta != 'sim':
    resposta = input('Deseja continuar no Loop ? ')
    resposta = resposta.lower()

