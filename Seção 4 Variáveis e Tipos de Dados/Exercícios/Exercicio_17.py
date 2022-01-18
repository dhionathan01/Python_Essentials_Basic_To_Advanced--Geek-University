"""
Leia um valor de comprimento em centímetros e apresente-o convertido em Polegadas.
A fórmula de conversão é:
P = C / 2.54

C =  Comprimento em centímetros
P = comprimento em polegadas
"""
C = float(input('Informe valor em centímetros: '))
P = C / 2.54
print(f'{C}cm equivale {P:.2f} polegadas')
