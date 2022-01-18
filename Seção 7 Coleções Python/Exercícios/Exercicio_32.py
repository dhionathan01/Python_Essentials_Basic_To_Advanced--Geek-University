"""
Leia dois vetores de inteiros x e y, cada um com 5 elementos(assuma que o usuário não onforma elementos repetidos).
Calcule e mostre os vetores resultatnes em cada caso abaixo:
* Soma entre x e y: soma de cada emento de x com o elementoda da mesma posição em y
* Produto entre x e y: multiplicação de cada emento de x com o elemento da mesma posição em y
* Diferença entre x e y: subtração de cada elento de x com o elemento da mesma posição em y
* Interseção entre x e y: todos os elementos de x que não existe em y
"""
x = []
while len(x) < 5:
    valor = int(input(f'Informe o {len(x)+1}° valor do vetor x: '))
    if valor not in x:
        x.append(valor)
    else:
        print('O valor Informado já existe dentro do vetor, e não será adicionado')
y = []
while len(y) < 5:
    valor = int(input(f'Informe o {len(y)+1}° valor do vetor y: '))
    if valor not in y:
        y.append(valor)
    else:
        print('O valor Informado já existe dentro do vetor, e não será adicionado')

soma = []
for i in range(len(x)):
    soma.append(x[i] + y[i])

produto = []
for i in range(len(x)):
    produto.append(x[i] * y[i])

diferenca = []
for i in range(len(x)):
    diferenca.append(x[i] - y[i])

intersection = []
for i in range(len(x)):
    if x[i] in y:
        intersection.append(x[i])
uniao = []
for i in range(len(x)):
    uniao.append(y[i])
    if x[i] not in y:
        uniao.append(x[i])

print(f'Tabela de somas: ')
for lista_somas in range(5):
    print(f'{x[lista_somas]} + {y[lista_somas]} = {soma[lista_somas]}')

print(f'Tabela de Protudos: ')
for lista_produto in range(5):
    print(f'{x[lista_produto]} x {y[lista_produto]} = {produto[lista_produto]}')

print(f'Tabela de Diferença: ')
for lista_diferenca in range(5):
    print(f'{x[lista_diferenca]} - {y[lista_diferenca]} = {diferenca[lista_diferenca]}')

print(f'Interseção da lista x e y:\n {intersection}')
print(f'União da lista x e y: \n {uniao}')
