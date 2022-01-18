"""
Crie um programa que recaba três valores (obrigatoriamente maiores que zero),
representando as medidas dos três lados de um triângulo. Elabore funçõs para:
1 — Determinar se os lados formam um triângulo.
2 — Determinar e mostra o tipo de triângulo caso as medidas formem um triângulo
    * Chama-se equilátero o triângulo que tem três lados iguais.
    * Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    * Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""


def determina_triangulo(lado1, lado2, lado3):
    if lado1 < lado2 + lado3 or lado2 < lado1 + lado3 or lado3 < lado2 + lado1:
        return True


def tipo_de_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        tipo = 'Equilátero'
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
    return tipo


medida = []
while len(medida) < 3:
    valor = (float(input(f'Informe a {len(medida)+1}° medida: ')))
    if valor > 0:
        medida.append(valor)
    else:
        print(f'Valor Inserida não pode ser menor que zero')
triangulo = determina_triangulo(lado1=medida[0], lado2=medida[1], lado3=medida[2])
print(triangulo)
if triangulo:
    tipo_triangulo = tipo_de_triangulo(lado1=medida[0], lado2=medida[1], lado3=medida[2])
    print(f'A figura informada é um triângulo: {tipo_triangulo}')
else:
    print(f'A figura informada não é triangulo')

