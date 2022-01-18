"""
O bloco try/except

Utilizamos o bloco try/excepet para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa
para de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
excepet:
    //o que deve ser feito em caso de problema
"""

# Exemplo 1 - Tratando um erro genérico

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem "Deu algum problema"
'''
try:
    geek()
except:
    print('Deu algum problema')
'''
# Exemplo 2

# Tente executar a função len(5), caso você encontre erros, imprima a mensagem "Deu algum problema"
'''
try:
    len(5)
except:
    print('Deu algum problema')
'''

"""
OBS: Tratar erro de forma genérica não é a melhor froma de tratamento de erros. O ideal é SEMPRE tratar de forma
específica.
"""

# Exemplo 3 - Tratando erro específico
'''
try:
    geek()
except NameError:
    print('Você está utilziando uma função inexistente')
'''
# Exemplo 4 - Tratando erro específico
'''
try:
    len(5)
except TypeError:
    print('Não é possível utilizar um objeto do tipo int em um len')
'''
# Exemplo 5 - Tratando erro específico com detalhes do erro
'''
try:
    len(5)
# Variável err recebe o erro
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
'''

# Exemplo 6 - Tratando erro específico com detalhes do erro

# Podemos efetuar diversos tratamentos de erros de uma vez.
'''
try:
    print('Geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print(f'Ocorreu um erro inesperado')
'''


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'Geek'}
print(pega_valor(dic, 'game'))
