"""
Usando switch, escreva um program que elia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este
número. iso é, domingo se 1, segunda-feira se 2, e assim por diante.
"""

# OBS: Em Python não existe switch, sendo assim o exercício será feito com if else
numero = float(input('Insira um número: '))
if numero == 1:
    print('Domingo')
elif numero == 2:
    print('Segunda-feira')
elif numero == 3:
    print('Terça-feira')
elif numero == 4:
    print('Quarta-feira')
elif numero == 5:
    print('Quinta-feira')
elif numero == 6:
    print('Sexta-feira')
elif numero == 7:
    print('Sábado')
else:
    print('Opção inválida')