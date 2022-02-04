"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional,
o softeware precisa ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de Escrita -> Para escrever o arquivo.

StringIO - > Utilizado para ler e criar arquivos em memória.
"""

# Para utilizar o StringIO, primeiro fazemos import

from io import StringIO

mensagem = 'Essa é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesma vazia para inserirmos texto depois

arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w') é a msm coisa que está sendofeita acima
# Porém o arquivo não está em disco e o nome é dado pelo próprio sistema operacional

# Agora tenddo o arquivo, podemos utilizar tudo que já sabemos

print(arquivo.read())

# Escrevendo outros textos
arquivo.write(' Outro texto')

# podemos inclusive movimentar o cursor
arquivo.seek(0)  # voltando o cursor pro ínicio
print(arquivo.read())  # lendo arquivo  novamente
