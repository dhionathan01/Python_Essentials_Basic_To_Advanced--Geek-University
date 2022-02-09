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
