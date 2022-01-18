"""
Faça uma função e um programa de teste para o cáculo do volume de uma esfera.
Sendo que o raio é passado por parâmetro.
"""


def calcularvalordaesfera(R):
    V = 4 / 3 * 3.14 * R ** 3
    return V


valor = float(input('Insira o Raio da esfera: '))
print(f'Volume da Esfera: {calcularvalordaesfera(valor):.2f}')
