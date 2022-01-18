"""
Módulo Collections - Default Dict
# Recapitulando Dicionários em Python.

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)   # Imprima todo o dicionário

print(dicionario['curso'])  # Imprima o valor do dicionário

# print(dicionario['outro'])    # Ao tentar imprimir o valor de uma chave inexistente gera KeyError

Defaul dict  -> Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar um lambda para
isso. Este valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que não existe,
essa chave será criada e o valor default será attribuído.

OBS: Lambdas são funções sem nome, que podem ou não receber um parâmetro de entrada e ternonar valores.
"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python Essencial'

print(dicionario)

print(dicionario['outro'])  # Keyerror no dicionário comum, mas aqui não.

print(dicionario)
