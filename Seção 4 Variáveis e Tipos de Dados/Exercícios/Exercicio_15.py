"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é:
R = G * r / 180
G = ângulo em graus
R = Radianos
r = 3.14 (Pi)
"""
G = float(input('Informe o Angulo a ser Convertido: '))
R = (G * 3.14) / 180
print(f'{G}° Equivale a {R:.2f} radianos')
