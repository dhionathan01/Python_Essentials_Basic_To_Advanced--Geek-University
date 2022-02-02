"""
O bloco with
Passo para se trabalhar com arquivos
# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 -  Fechamos o arquivo

o block with é utilizado para criar um contexto de trabalho onde os recursos utilizados
são fechados após o bloco with

"""

# o bloco with

with open('texto_leitura_de_arquivos.txt', encoding='utf-8') as arquivo:
    print(arquivo.readline())
    print(arquivo.closed)

# print(arquivo.read()) Um erro ocorrerá pois o arquivo já foi fechado
print(arquivo.closed)
