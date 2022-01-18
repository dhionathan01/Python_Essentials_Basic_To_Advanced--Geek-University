"""
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral.
"""
notas = []

while len(notas) < 15:
    nota = float(input(f'Insira a nota do aluno 0{len(notas)+1}: '))
    notas.append(nota)

print(f' Notas dos alunos: {notas}')
print(f' Média Global da Turma: {sum(notas)/len(notas)}')
