"""
Funções com Parâmetro (de entrada)

 - Funções que recebem dados para serem processados dentro da mesma.
Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída
Se a gente pensar em função, já sabemos que temos funções que:
 - Não possuem entrada.
 - Não possuem saída.
 - Possuem entrada mas não possuem saída.
 - Não possuem entrada mas possuem saída.
 - possuem entrada e saída.


"""

# Refatorando uma função

"""
def quadrado(numero):
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)
"""
# Refatorando a função

'''
def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')
    return ''


print(cantar_parabens('Dhioanthan'))
'''

"""
Funções podem ter váriaos parâmetros de entrada. Ou seja, podemos receber como entrada em uma função quantos para
metros forem necessários. eles são separados por vírgula.
"""

'''
def soma(a, b):  # Recebendo dois parâmetros.
    return a + b


def multilplica(num1, num2):  # Recebendo dois parâmetros.
    return num1 * num2


def outra(num1, b, msg):  # Recebendo três parâmetros.
    return (num1 + b) * msg


print(soma(2, 5))  # Enviando 2 argumentos para 2 paramêtros
print(soma(10, 20))  # Enviando 2 argumentos para 2 paramêtros

print(multilplica(4, 5))  # Enviando 2 argumentos para 2 paramêtros
print(multilplica(2, 8))  # Enviando 2 argumentos para 2 paramêtros

print(outra(3, 2, 'Geek'))  # Enviando 3 argumentos para 3 paramêtros
print(outra(5, 4, 'Python'))  # Enviando 3 argumentos para 3 paramêtros


#  OBS: Se a gente informar um número errado de parâmetros ou argumentos, teremos TypeError

# print(soma(2, 3, 4))  # TypeError - Passando argumentos a mais
# print(soma(4))  # TypeError - Passando argumentos a menos
'''

'''
# Nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

# A diferença entre parâmetros e Argumentos

# Parâmetros são variáveis decalaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função


# A ordem dos parâmetros importa !!!

nome = 'Felicity'
sobrenome = 'Jones'
#                    argumento 1, argumento 2
print(nome_completo(sobrenome, nome))

# Observe que a exibição sai inversa devido a forma que foi enviado os argumentos

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem

print(nome_completo(nome='Dhionathan', sobrenome='Jobim'))
print(nome_completo(sobrenome=sobrenome, nome=nome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))
'''

# Erro comum na utilização do return

'''
def soma_impares(numeros):  # Errado
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total  # O return encerra a função então logo que entrar no if a função sera encerrada, por tanto o
        # o return deve ficar fora do if, para que função funcione de forma correta.
'''


def soma_impares(numeros):  # Certo
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


if __name__ == '__main__':  # Corrigi o arquivo para ser um módulo
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))
    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
else:
    print('O módulo funcoes_com_parametro.py foi importado.')