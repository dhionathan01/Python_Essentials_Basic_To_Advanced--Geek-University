"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é:
C = P * 2.54

C =  Comprimento em centímetros
P = comprimento em polegadas
"""
P = float(input('Informe valor em Polegadas: '))
C = P * 2.54
print(f'{P} polegadas equivale {C}cm')
