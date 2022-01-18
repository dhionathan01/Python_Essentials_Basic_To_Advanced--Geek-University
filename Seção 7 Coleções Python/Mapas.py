"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}
"""
'''
receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Interar sobre dicionários

# Para cada chave em receita, imprima a chave.
for chave in receita:
    print(chave)

# Para cada chave em receita, imprima seu valor
for chave in receita:
    print(receita[chave])
# Para cada chave em receita , imprima a chave e o valor
for chave in receita:
    print(f'{chave}:{receita[chave]}')

# Acessando as chaves.
print(receita.keys)

# Forma Pythônica de se fazer:
for chave in receita.keys():
    print(receita[chave])
'''

'''
# Acessando Valores.
receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

print(receita.values())

for valor in receita:
    print(valor)

# Desempacotamento de dicionários

print(receita.items())
# Para cada indice e valor contido no dicionário receita: imprima chave e valor.
for chave, valor in receita.items():
    print(f'chaves: {chave} valor: {valor}')
'''
# *Soma, *Valor Máximo, *Valor Mínimo, Tamanho.

# * Se os valores forem todos inteiros ou reais.

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(sum(receita.values()))  # Soma
print(max(receita.values()))  # Valor Máximo (maior).
print(min(receita.values()))  # Valor Mínimo (menor).
print(len(receita))           # Total de índices preenchidos.
