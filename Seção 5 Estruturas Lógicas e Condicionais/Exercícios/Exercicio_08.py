"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas.
Uma nota válida deve ser obrigatoriamente um valor entre 0.0 e 10.0, onde caso a nota não possua um valo válido,
este fato deve ser informado ao usuário e o programa termina.

"""
import sys

nota1_validade = True
nota2_validade = True
nota1 = float(input('Insira a Nota 1 do Aluno: '))
if 0.0 <= nota1 <= 10.0:
    nota1_valida = True
else:
    nota1_validade = False

nota2 = float(input('Insira a Nota 2 do Aluno: '))
if 0.0 <= nota2 <= 10.0:
    nota2_validade = True
else:
    nota2_validade = False

if nota1_validade and nota2_validade is True:
    print(f'Nota 01: {nota1}')
    print(f'Nota 02: {nota2}')
    print(f'As notas são válidas')
    print(f'Média do Aluno: {(nota1+nota2)/2}')

else:
    print('Uma ou mais Notas são inválidas')
    sys.exit()
