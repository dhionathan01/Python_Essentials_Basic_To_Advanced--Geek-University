"""
A nota final de um estudante é calculada a partir de três notas atribúidas entre o intervalo de 0 até 10,
respectivamente, a um trabalho de laboratório, a uma avaliação semestreal e a um exame final. A médida das três notas
mencionadas anteriormente obedece aos pesos: trabalho de laboratório: 2 Avaliação Semestreal: 3; Exame final: 5.
De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação(entre 3 e 4,9)
Ou aprovado. Faça todas as verificações necessárias
"""
trabalho_de_labotorio = (float(input('Informe a nota do trabalho de laboratório : ')))
avaliacao_semestreal = (float(input('Informe a nota da avaliação semestral : ')))
exame_final = (float(input('Informe a nota do exame final : ')))
nota = (2 * trabalho_de_labotorio + 3 * avaliacao_semestreal + 5 * exame_final)/(2+3+5)
print(f'{nota:.2f}')
if nota < 2.9:
    print('Aluno Reprovado')
elif 3 <= nota <= 4.9:
    print('Recuperação')
elif nota >= 5:
    print('Aluno Aprovado')