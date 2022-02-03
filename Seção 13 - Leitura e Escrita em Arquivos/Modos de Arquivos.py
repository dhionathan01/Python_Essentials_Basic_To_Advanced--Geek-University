"""
Modos de Arquivos

r -> Abre para leitura - Padrão

w -> Abre para escrita -  sobrescreve caso o arquivos já exista

x -> Abre(cria) para escrita - somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError.

a -> Abre para escrita - adicionando o conteúdo ao final do arquivo.
# OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo será
adicionado SEMPRE ao final do arquivo. Com o modo 'a' não controlamos o cursor

+ -> Abre para o modo atualização leitura e escrita

http://docs.python.org/3/library/functions.html#open
"""

# Modo de abertura x
'''
try:
    with open('university.txt', 'x', encoding='utf-8') as arquivo:
        arquivo.write('Teste de conteúdo2. \n')
except FileExistsError:
    print('Arquivo já existe')
'''

# Modo de abertura 'a'
'''
with open('frutas.txt', 'a', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe um fruta ou digite sair:')
        if fruta.lower() != 'sair':
            arquivo.write(f'{fruta}\n')
        else:
            break
'''

# OBS: Com o modo 'a' não controlamos o cursor
'''
with open('outro.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Normal text\n')
    arquivo.write('Normal text\n')
    arquivo.seek(0)
    arquivo.write('No topo!\n')
    arquivo.write('Novalinha\n')
'''

with open('outro.txt', '+', encoding='utf-8') as arquivo:
    arquivo.write('Normal text\n')
    arquivo.write('Normal text\n')
    arquivo.seek(0)
    arquivo.write('No topo!\n')
    arquivo.write('Novalinha\n')