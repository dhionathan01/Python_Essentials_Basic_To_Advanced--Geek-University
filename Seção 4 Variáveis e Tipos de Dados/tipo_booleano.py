"""
Tipo Booleano

Álgebra Booleana, criada por George Boole

2 constatnes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso
OBS: Sempre com a inicial maiúscula

Errado:

true, false

Certo:

True, False
"""
ativo = True
print(ativo)

"""
Operações básicas :
"""

# Negação (Not)
"""
Fazendo a Negação, se o valor do booleano for verdadeiro o resultado retornado será falso,
se for falso o resultado será verdadeiro. A negação retornara sempre o contrário da afirmação da variável
"""
print(not ativo)

logado = True
# Ou (or)
"""
è uma Operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.
True or True -> True
True or False -> True
False or True -> True
False or False -> False

"""
print(ativo or logado)
# resultado -> True

logado = False
ativo = False
print(ativo or logado)
# resultado -> False

# E (and):
"""
Também é uma operação binária, ou seja, depende de deois valores. Ambos os valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""