"""
Leia um ângulo em graus e apresente-o convertido em radianos.
A formula de conversão é:
R = G * r(3,14) / 180
Sendo
G = O angulo em graus
R = Radianos
r = 3.14
"""
G = float(input('Digite o valor em Graus: '))
R = (G * 3.14) / 180
print(f'{G}° Graus Equivale: {R:.2f}° Radianos ')
