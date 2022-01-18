"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is
Regras de funcionamento:
- Para o 'and', ambos os valores precisam ser True.
- Para o 'or', somente um ou outro precisa ser True.
- Para o 'not', o valor do booleano é invertido, ou seja, caso uma sentença seja True vira false, se for false vira true
- Para o 'is', o valor é comparado com um segundo.
"""
ativo = False
logado = True
'''
# Testando 'and'
if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta por favor, cheque seu e-mail')
'''
'''
# Testando or
if ativo or logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta por favor, cheque seu e-mail')
'''
'''
# Testando not
if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo Usuário')
'''

# Testando is
if ativo is False:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo Usuário')

# ativo é True?
print(ativo is True)
