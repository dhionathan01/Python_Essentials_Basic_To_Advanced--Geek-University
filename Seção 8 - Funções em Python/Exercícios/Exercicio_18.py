"""
Faça uma função que recaba por parâmetro dois valores X e Z. Cacule e retorne o resultado X elvado a Z
para o programa principal, Atenção não use nenhuma função pronta de exponenciação.
"""


def calcular_potencia(X, Z):
    resultado = 1
    for i in range(Z):
        resultado = resultado * X
    return resultado


valor_base = float(input('Informe o valor Base: '))
potencia = int(input('Informe o valor da elevação : '))
total = calcular_potencia(valor_base, potencia)
print(f'{valor_base} ^ {potencia}: {total}')

