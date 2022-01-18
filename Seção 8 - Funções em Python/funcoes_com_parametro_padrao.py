"""
Funções com Parâmetro Padrão ( Defaul Paramaters)

- Funções onde a passagem de parâmetro seja opcional:

# Exemplo de função onde a passagem de parâmetro seja opcional

print('Geek University')
print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2


print(quadrado(3))

print(quadrado()) # TypeError
"""

'''
def exponencial(numero, potencia=2):  # Ao colocar um valor padrão nas váriaveis, eles se tornam opcionais
    return numero**potencia


print(exponencial(2, 3))    # 2 * 2 * 2 = 8
print(exponencial(3, 2))    # 3 * 3 = 9

print(exponencial(3))   # Por padrão elevado ao quadrado
print(exponencial(3, 5))    # Eleva á Potência Informada pelo usuário
'''

"""
OBS:
 -  Se o usuário passar somente 1 argumento ste será atribúido ao parâmetro número, e será calculado o quadrado deste
 número devido o fato de que tornamos a o argumento potencia opcional ao já definimos um valor padrão "potencia=2".
 - Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro numero e o segundo ao parâmetro potencia
 pois substituira o valor 2 predefinido na potencia em "potencia=2", então sera calculada a potencia.
 então sera calculada esta potencia.

"""

# OBS: Em funções Python, os parâmetros com valores dafault (padrão) DEVEM sempre estar ao final da declaração.

# ERRO!
'''
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))
'''

# Outros Exemplos

# ERRO
'''

def soma(num1, num2):
    return num1 + num2


print(soma(4, 3))
# print(soma(4))  # TypeError
# print(soma())   # TypeError

#CERTO !


def soma(num1=1, num2=1):
    return num1 + num2


print(soma(4, 3))
print(soma(4))
print(soma())  
'''


# Exemplo mais complexo
'''
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem Vindo Instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

# Porque Utilizar parâmetros com valor default ?
 - Nos permite ser mais flexíveis nas funções;
 - Evita erros om parâemtros incorretos;
 - Nos permite trabalhar com exemplos mais legíveis de código;
 
# Quais tipos de dados podemos utilizar como valores default para parâmetros ?

 - Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;
'''

# Exemplos Utilizando funções como argumento e parâmetro na execução de outra função

'''
def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))
'''

# Escopo - Evitar problemas ae  confusões...

# Variáveis glboais
# Variáveis locais
'''
instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = 'Python'    # Variável local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência
'''

'''
def diz_oi():
    prof = 'Geek'   # Variável Local
    return f'Olá {prof}'


print(diz_oi())

# print(prof) # NameErro
'''
"""
 Esse erro ocorre porque estamos tentando printar uma variável que não existe, pois ela foi declarada localmente,
 dentro da função logo ela n existe fora dela
"""

# Atenção com variáveis globais (Se puder evitar, evite!)

'''
#ERRO!
total = 0


def incrementa():
    # total = total + 1  # UnboundLocalError (A variável local está sendo utilizada para processamento sem ser iniciada)
    return total

print(incrementa())
'''

# CORRETO
'''
total = 0


def incromenta():
    global total    # Avisando que queremos utilizar a variável global

    total = total + 1
    return total


print(incromenta())
print(incromenta())
print(incromenta())
print(incromenta())
'''

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável.


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Está variável não é local nem global, ele pertence a função anterior.
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())
print(fora())