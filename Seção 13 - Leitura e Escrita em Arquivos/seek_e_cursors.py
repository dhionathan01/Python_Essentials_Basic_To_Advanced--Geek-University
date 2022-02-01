"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo. seek significa -> Procurar

"""

'''
arquivo = open('texto_leitura_de_arquivos.txt', encoding='utf-8')
print(arquivo.read())

# seek() - > Ela recebe um parâmetro que indica onde queremos colocar o cursor.

arquivo.seek(0)  # Exemplo na posição 0, no início do arquivo
print(arquivo.read())

arquivo.seek(22)  # Movendo o cursor para o caracter 22
print(arquivo.read())  # Lendo o arquivo apartir do caracter 22
'''

'''
arquivo = open('texto_leitura_de_arquivos.txt', encoding='utf-8')

# readline() -> Função que lê o arquivo linha a linha. readline -> Lê linha
# print(arquivo.readline())

ret = arquivo.readline()
print(type(ret))
print(arquivo.readline())
print(ret.split(' '))
'''

'''
arquivo = open('texto_leitura_de_arquivos.txt', encoding='utf-8')

# readlines() -> Leia as linhas
linhas = arquivo.readlines()
print(linhas)
print(len(linhas))  # retorna quantas linhas tem o arquivo, caso a última linha estiver vazia, ela não é somada
'''
"""
OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming.
Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilziamos a função close()

Passos para se trabalhar com um arquivo:
1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;
"""

'''
# 1 - Abrir o arquivo;
arquivo = open('texto_leitura_de_arquivos.txt')

# 2 - Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado
# 3 - Fechar o arquivo;
arquivo.close()

print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado

# print(arquivo.read())
# OBS: Se tentarmos manipular o arquivo após o seu fechamento, teremos um ValueError
'''
