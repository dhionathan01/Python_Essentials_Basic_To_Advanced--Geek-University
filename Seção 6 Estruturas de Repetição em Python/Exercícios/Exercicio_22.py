"""
Escreva um programa completo que pemrita a qualquer aluno introduzir,
pelo teclado, uma sequência arbitrária de notas(válidas no intervalo de 10 a 20)
e que mostre na tela, como resultado a correspondente média aritmética.
O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao pgroama, o qual terminará quando
for introduzido um valor que não sejá valido como nota de aprovação.
"""
soma = 0
contador = 0
valor = float(input('Insira um valor válido: 10 a 20: '))
if 20 >= valor >= 10:
    while 20 >= valor >= 10:
        print(valor)
        soma += valor
        valor = float(input('Insira um valor válido: 10 a 20: '))
        contador += 1
else:
    print('Número inserido inválido')

print(f'O valor: {valor} é inválido, sequência de incremento de notas interrompida')
try:
    print(f'A média aritmética dos valores válidos inseridos equivale: {soma/contador}')
except ZeroDivisionError:
    contador = 1
