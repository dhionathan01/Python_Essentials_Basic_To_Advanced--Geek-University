"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a se gunda prova tem peso 1 e a
terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi parovado ou reprovado. A nota para
aprovação deve ser igual ou superior a 60 pontos
"""
nota1 = float(input('Insira a Nota 01: '))
nota2 = float(input('Insira a Nota 02: '))
nota3 = float(input('Insira a Nota 03: '))

nota_total = (nota1+nota2+nota3) / 4
print(f'Média total: {nota_total}')

if nota_total >= 60:
    print('Aluno Aprovado')
else:
    print('Aluno Reprovado')
