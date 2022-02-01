"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada,
que neste caso é o caminho para o  arquivo que deve ser lido. Essa função retorna um _io.TextIOWrapper
e é com que que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a funçao open() abre o arquivo para leitura.
Este arquivo deve exitir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto_leitura_de_arquivos.txt' mode='r' encoding='cp1252'>

more r -> Modo de Leitura. r -> read() -> Ler

"""

# Exemplo

arquivo = open('texto_leitura_de_arquivos.txt', encoding='utf-8')

# print(arquivo)

# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

# print(arquivo.read())

"""
OBS: O Python, utiliza um reurso apra trabalhar com arquivos chmado cursor.
Esse cursor, funciona como o cursor quando estamos ecrevendo.
"""
# print(arquivo.read())

# O segundo print não é exibido pois o cursor já leu todos os caracters do arquivo,e manteve
# o cursor em sua última posição

# OBS: A função read() lê todo o conteúdo do arquivo.

ret = arquivo.read()
print(type(ret))
print(ret)
