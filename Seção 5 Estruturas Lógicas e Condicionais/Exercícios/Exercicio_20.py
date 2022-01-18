"""
Dados tres valores, A,B,C verificar se eles podem ser os valores dos lados de um triângulo,
E se forem determinar se o triângulo é escaleno, equilátero ou sióscele, considere os seguintes conceitos:

* O Comprimento de cado lado de um triângulo é menor do que a soma dos outros dois lados
* Chama-se equilátero o triângulo que tem três lados iguais.
* Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
* Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""
A = float(input('Informe o comprimento do lado A: '))
B = float(input('Informe o comprimento do lado B: '))
C = float(input('Informe o comprimento do lado C: '))

triangulo = None
# O Comprimento de cado lado de um triângulo é menor do que a soma dos outros dois lados
if A < B + C and B < C + A and C < B + A:
    triangulo = True
    print('A figura correponde a um Triângulo')
else:
    triangulo = False
    print('A figura não é um Triângulo')
if triangulo:
    if A == B and A == C:
        # Chama-se equilátero o triângulo que tem três lados iguais.
        print('O triângulo Correspondente é um Triângulo Equilátero')
    elif A == B or A == C or B == C:
        # Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
        print('O triângulo Correspondente é um Triângulo Isósceles')
    elif A != B and A != C and B != C:
        # Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
        print('O triângulo Correspondente é um Triângulo Escaleno')
    else:
        print('Sentença inválida')
