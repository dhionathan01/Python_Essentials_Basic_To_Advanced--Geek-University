"""
Sistemas de Arquivos - Navegação:

Para fazer uso de manipulação de arquivo do sistema operacional, precisamos importar
e fazer udo do módulo os.

OS - Operating sustem - Sistema operacional
"""

# Fazer o import
import os
'''
#   getcwd() -. Pega o current work directory - diretório de trabalho (corrente/atual)
# Retorna o path(caminho) absoluto
print(os.getcwd())

# Para mudar o diretório, podemos utilziar o chdir()
os.chdir('..')  # vai para o diretório anterior
print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo
# os.path.isabs = O diretório informado é absoluto ?
print(os.path.isabs('C:/Users/dhion'))  # True(verdade) visto que é C:/ é o diretório raiz
# Opcional = ('C:\\Users\\dhio'))
print(os.path.isabs('Users/dhion'))  # False(falso) visto que é C:/ é o diretório raiz, e ele não foi informado

# OBS Para usuários windows
# Se você estiver utilizando um computador com windows, terá que ter cuidado ao verifiar diretórios

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
# print(os.uname()) para Linux e Mac
print(os.getcwd())  # C:\\Users\\dhion\Documents\\Git\\Udemy--Curso--Python
# o "os.path.join" concatena o diretório de acordo com o sistema operacional
direct = os.path.join(os.getcwd(), 'Seção 13 - Leitura e Escrita em Arquivos', 'testando')
print(direct)
os.chdir(direct)
print(os.getcwd())
'''

'''
# Podemos Listar os arquivos e diretórios com o listdir()
print(os.listdir())
print(f'Número de arquivos: {len(os.listdir())}')

# Podemos Listar os arquivos e diretórios com mais detalhes com scandir()
print(os.scandir('C:\\'))
print(list(os.scandir('C:\\')))
'''
# Pegando detalhes de um determinado arquivo
scanner = os.scandir()
arquivo = list(scanner)
print(arquivo)
print(dir(arquivo[0]))
print('Detalhes: ')
print(arquivo[0].inode()) # ??
print(arquivo[0].is_dir())  # É um diretório ? False
print(arquivo[0].is_file())  # É um arquvio ? True
print(arquivo[0].is_symlink())  # É um link simbólico ? False
print(arquivo[0].name)  # Nome do arquivo
print(arquivo[0].path)  # Caminho até o arquivo
print(arquivo[0].stat())  # Estatísicas...

# OBS: Quando utilziamos a função scandir() nós precisamos fecha-la, assim quando abrimos um arquivo.

scanner.close()