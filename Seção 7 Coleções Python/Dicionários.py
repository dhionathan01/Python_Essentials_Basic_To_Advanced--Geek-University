"""
Dicionários

OBS: Em algumas linguagens de programação os dicinários python são conhecidos por mapas.

- Dicionários são colenções do tipo chave/ valor.
    OBS: No caso das listas e tuplas a chave é o índice, que apesar de sabermos, ele não é exibido, por isso dizemos
    que nas listas e tuplas, sua chave é implícita

- Dicionários são representados por chaves {}.
    print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor'.
    - Tanto chave quanto valor podem ser de qualquer tipo de dado.
    - Podemos misturar tipos de dados.
"""

'''
# Criação de Dicionários

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai', }
print(paises)

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises)
print(type(paises))
'''

'''
# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai', }

print(paises['br'])
# print(paises['ur'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError.

# Forma 2 - Acessando via get - Recomendada
# OBS: Diferente da forma 1, utilizando o get, a chave sera retornada como vazia, e logo não ocorrerá KeyError.

print(paises.get('br'))
print(paises.get('ru'))
'''
'''
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai', }
"""
Observe que não existe a chave 'ru' logo paises.get('ru') retornara None, que entendido como false
assim entrando diretamente no else.
"""
pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print(f'Não encontrei o país')
'''

'''
# Forma alternativa, sem o uso do if else
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai', }

pais = paises.get('ru', 'Não encontrado')  # Podemos definir um valor padrão caso não encontremos o objeto.
"""
# A cima estamos definindo para que caso a chave não exista, ou esteja vazia, preencher a mesma com 'Não encontrado'.
Assim tornando não necessário o uso do if e else.
"""
print(pais)
'''

'''
# Podemos verificar se determinada chave se encontra em um dicionário.

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai', }

print('br' in paises)  # True
print('ru' in paises)  # False
print('Estados Unidos' in paises)  # False - Estados Unidos se trata de um valor e não chave.
'''
'''
# Podemos utilizar qualquer tipo de dado ( int, float, string, boolean), inclusive lista, tupla, dicionário
# como chaves de dicionário.
# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários,
# pois as mesmas são imutáveis.

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))
'''
'''
# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai': 600})
print(receita)
# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# Tecnciamente Utilizamos um processo de sobscrever os dados.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas
'''
'''
# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Forma 1 Mais comum
print(receita)
ret = receita.pop('mar')
print(ret)
print(receita)
# OBS 1: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objetio é sempre retornado.

# Forma 2
del receita['fev']
print(receita)
# Se a chave não existir será gerado um KeyError.
# OBS: Neste caso o valor removido não é retornado.
'''

# Exemplo de onde e como usar dicionários:

"""
- Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de compras:
    Produto 1:
        - nome:
        - quantidade:
        - preco:
    Produto 2:
        - nome:
        - quantidade:
        - preco:
"""
'''
# 1 - Poderiamos utilizar uma lista pra isso ? Sim

carrinho = []

produto1 = ['XBOX ONE', 1, 1999.99]
produto2 = ['Halo MCC', 1, 100.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Um detalhe é que teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderiamos utilizar uma Tupla para isso? Sim

produto1 = ('XBOX ONE', 1, 1999.99)
produto2 = ('Halo MCC', 1, 100.00)
carrinho = (produto1, produto2)
print(carrinho)

# Porém do mesmo jeito que na lista também teriamos que saber o índice de cada informação do produto.

# Poderiamos utilizar um dicionário para isso? Sim

carrinho = []
produto1 = {'nome': 'XBOX ONE', 'quantidade': 1, 'preco': 1999.99}
produto2 = {'nome': 'Halo MCC', 'quantidade': 1, 'preco': 100.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
# Desta forma, facilmente adicionamos ou removemos produtos no Carrinho e em cada produto
# podemos ter a certeza sobre cada informação.
'''

'''
# Métodos de dicionários.
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))
# Limpando o dicionário ( Zerar dados)
d.clear()
print(d)
'''
# Copiando um dicionário para outro
'''
# Forma 1 - Deep Copy
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))
novo = d.copy()
print(novo)

novo['d'] = 4
print(d)
print(novo)
'''

'''
# Forma 2 # Shallow Copy
d = dict(a=1, b=2, c=3)
novo = d

print(novo)
novo['d'] = 4
print(d)
print(novo)
'''
# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))
# O método fromkeys recebe dois parâmetros: um interável e um valor.
# Ele vai gerar para cada valor do ite´ravel uma chave e irá atribuir a esta chave o valor informado.

# Curiosidade - Lembrese que o python, não difere na identificação de char e string como em outras linguagens
# Observe:

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
