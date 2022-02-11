"""
Sistema de arquivos - Manipulação
"""

import os
'''

# Descobrindo se um arquivo existe
print(os.path.exists('arquivo.txt'))    # False
print(os.path.exists('frutas.txt'))    # True
'''
# Descobrindo se um diretório existe
'''
# Paths relativos
print(os.path.exists('testando'))   # True
print(os.path.exists('testando/testando_diretorio'))    # True
print(os.path.exists('outro'))    # false
# Paths absolutos
print(os.path.exists('C:/Users/dhion/OneDrive/Documentos/Bloco de anotações de Dhionathan.url'))  # True
print(os.path.exists('C:/Users/dhion/OneDrive/Documentos/img'))  # False
'''


# Criando arquivos - Formas possíveis
# Forma1
# Cria o arquivo com o comando opencaso o mesmo não existir, e fecha com o .close
'''
open('arquivo_test.txt', 'w', encoding='utf-8').close()

# Forma2
open('arquivo_test2.txt', 'a', encoding='utf-8').close()

# Forma3
with open('arquivo_test3.txt', 'w', encoding='utf-8') as arquivo:
    pass  # Não faça nada
'''
"""
OBS: Quando abrimos um bloco e não queremos fazer nada colocamos o pass, a ausencia dele o compilador reclamaria
da ausência de identação
"""
# Forma correta de criar arquivo - não disponível pra windows
# os.mknod('arquivo_test4.txt')

# Criando diretórios Únicos (Um a Um)
'''
os.mkdir('templates')  # Relativo

os.mkdir('C:/Users/dhion/Documents/Git/Udemy--Curso--Python/Seção 13 - Leitura e Escrita em Arquivos')  # Absoluto
'''
# OBS: A função mkdir cria um diretório se este não existir, caso exista, teremos FileExistsError
# OBS: Caso não tenhamos permissão para criar o diretório termos o erro PermissionError

# Erro pois eles ta tentando criar o o diretório testando_novo_dir em novodir, sendo que o msm não existe
# os.mkdir('templates/novodir/testando_novo_dir')

# A alternativa que temos é o makedirs(Faça diretórios):

# Criando multi-diretórios (árvore de diretórios)

# os.makedirs('templates/novodir/testando_novo_dir')

# OBS: Caso exista, teremos FileExistsError

# os.makedirs('templates2/novo2/outro2', exist_ok=True)

# OBS: exist_ok=True Faz com que caso o diretório exista apenas ignore e não exiba erros

# Renomear arquivos e diretórios
# Diretórios

# os.rename('templates2', 'Renomeando_Templates2')

# OBS: Se o diretório não existir teremos um FileNotFoundError
# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Renomeando arquivos:
# Renomeando arquivo : teste12314.txt, para rename_test.txt

# os.rename('templates/novodir/testando_novo_dir/teste12314.txt', 'templates/novodir/testando_novo_dir/rename_test.txt')

# Renomeando arquivo frutas.txt para cesta_frutas.txt
# os.rename('frutas.txt', 'cesta_frutas.txt')

# Atenção! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles não vo para lixeira

# Deletando arquivos

# os.remove('arquivo_test.txt')

# OBS: Se você estier no Windows eo arquivo que você for deletar estiver em uso, você tera um erro.
# OBS: Se o arquivo não existir teremos um FileNotFoundError
# OBS: Caso informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

# Removendo diretórios vazios

# os.rmdir('templates')

# OBS: Se o diretórui tiver qualquer conteúdo teremos OSError
# OBS: Se o diretório não existir teremos um FileNotFoundError

# Criando 1000 arquivos text para testar o comando removendo uma árvore de diretórios:
'''
for i in range(1000):
    open(f'testando/arquivo_test{i+1}.txt', 'w', encoding='utf-8').close()
'''
'''
# Removendo uma árvore de diretórios
for arquivo in os.scandir('testando'):
    if arquivo.is_file():
        os.remove(arquivo.path)
    if not arquivo.is_file():
        os.rmdir(arquivo.path)
'''

# Removendo um árvore de diretórios vazios:

# Fazendo os diretórios para teste:
# os.makedirs('Renomeando_Templates2/novo2/outro2')

# Removendo os diretórios:
# os.removedirs('Renomeando_Templates2/novo2/outro2')  # Remove todos os diretórios informados
# Se algum dos diretórios contiver arquivos ou outros diretórios o proesso para.
# ATENÇÃO: Ao remover os arquivos e diretórios com python eles não vão para lixeira. Eles são excluídos permanentemente

# Para mandar os arquivos para lixeira, precisamos de uma biblioteca de terceiros, então precisamos baixa:
# Comando: pip install send2trash
# Em caso de erro instale o lsb-core comando: pip install lsb-core

# Importando send2trash para uso:
from send2trash import send2trash

# Criando arquivos para teste
'''
open('cesta1.txt', 'w', encoding='utf-8').close()
open('cesta2.txt', 'w', encoding='utf-8').close()
'''

os.remove('cesta1.txt')  # Exclusão permamente Não vai para lixeira / Não é possível recuperar
send2trash('cesta2.txt')  # Vai para lixeira pode ser restaurado

