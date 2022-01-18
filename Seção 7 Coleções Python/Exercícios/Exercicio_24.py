"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o nome do aluno
segundo repsentando a sua altura em metros.
Encontre o aluno mais baixo e o mais alto.
Mostre o nome do aluno mais baixo e do mais alto, com suas alturas.
"""


def verificar_maior(lista_alunos):
    maior_valor = max(lista_alunos.values())
    for chave, valor in lista_alunos.items():
        if valor == maior_valor:
            return chave


def verificar_menor(lista_alunos):
    menor_valor = min(lista_alunos.values())
    for chave, valor in lista_alunos.items():
        if valor == menor_valor:
            return chave


alunos = {}

while len(alunos) < 10:
    nome = input('Insira o nome do aluno: ')
    if nome not in alunos:
        altura = float(input('Insira a altura de um aluno: '))
        aluno = {nome: altura}
        alunos.update(aluno)
    else:
        print('Alunos existente')

print(alunos)

print(f'Aluno Mais Alto:\n{verificar_maior(alunos)} Altura:{max(alunos.values())}')
print(f'Aluno Mais Baixo:\n{verificar_menor(alunos)} Altura: {min(alunos.values())}')
