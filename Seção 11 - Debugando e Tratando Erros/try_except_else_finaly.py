"""
Try / Excepet / Else / Finally

Dica de quando e onde tratar código:

 - TODA ENTRADA DEVE SER TRATADA

OBS: A função do usuário é DESTRUIR o seu sistema.
"""
'''
num = 0
try:
    num = int(input('Informe um número : '))
except ValueError:
    print('Valor incorreto')
print(f'Você digitou {num}')

# OBS: O código é sequencial, msm que entre na exceção a linha responsável por imprimir o número digitado é executada
# Veja como tratar isso abaixo:
'''

'''
try:    # Tente executar
    num = int(input('Informe um número:'))
except ValueError:  # Em caso de um ValueError, execute o seguinte código
    print('Valor Incorreto')
else:   # Senão ocorrer um except, execute o seguinte o código
    print(f'Você digitou {num}')

# Else -> é executado somente se não ocorrer o erro.
'''

'''
# Finally

try:
    num = int(input('Informe um número:'))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')
print('Depois do Bloco try/except')

# OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.

# O finally, geralmente, é utilziado para fechar ou desalocar recursos.
'''

# Exemplos mais complexo ERRADO:
'''
def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro número: '))
try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')
try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')
'''

# Exemplos mais complexo CORRETO:
"""
# OBS : Você é responsável pelas entradas das suas funções. Então, trate-as!
"""

'''
# OBS: Toda entrada deve ser validada
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))
'''

'''
# Exemplo mais complexo - Genérico
def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))
'''


# Exemplo mais complexo - Semi-Genérico
def dividir(a, b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))
