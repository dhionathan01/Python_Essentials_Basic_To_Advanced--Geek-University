"""
Leia um valor de volume em metros cúbicos m3 e apresente-o convertido em litros.
A fóruma de conversão é:
L = 1000 * M
L = volume em Litros
M = Metros cúbicos
"""
M = float(input('Informe quantos metros cúbicos devem ser convetidos: '))
L = 1000 * M
print(f'{M} metros cúbicos equivale a {L} litros')

