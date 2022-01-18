"""
Entedendo o **kwargs

Poderiamos chamar este parâmetro de qualquer coisa, por exemplo **xis, mas por conveção chamamos de **kwargs
Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige que
utilizemos parâmetros nomeados, e transforma esses parâmetros extras num dicionário.
"""

# Exemplo

'''
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()

cores_favoritas(geek='navy')
'''

'''
def cumprimento_especoal(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você Recebeu um cumprimento Pythônico Geek!'
    elif'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é...'


print(cumprimento_especoal())
print(cumprimento_especoal(geek='Python'))
print(cumprimento_especoal(geek='Oi'))
print(cumprimento_especoal(geek='especial'))
'''
"""
Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios:
- *args;
- Parâmetros default(não obrigatórios)
- **kwargs
"""

'''
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)
'''

'''



# Função na ordem correta
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]
# Saída:  [1, 2, (3,), 'Geek', {'sobrenome': 'University', 'cargo': 'Instrutor'}]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))
'''

'''
# Função com a ordem incorreta de parâmetros
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))
# Saida: [1, 2, (), 3, {'sobrenome': 'University', 'cargo': 'Instrutor'}]
'''

'''
# Desempacotar com **kwargs
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))
'''

'''
# Observe que podemos desempcotar dados, mesmo que  a função n tenha *args ou **kwargs definindo.
def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = [1, 2, 3]
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)


dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)
'''


# OBS: Os nomes da chave em um dicionário devem ser o mesmo dos parâmetros da função
def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


# dicionario = dict(d=1, e=2, f=3) # TypeError
# soma_multiplos_numeros(**dicionario)


