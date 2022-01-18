"""
Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km.h(quilômetros por hora).A fórmula de
conversão é:
* K = km/h
* M = m/s

K = M * 3.6

"""

M = float(input('Informe o valor em m/s a ser convertido : '))
K = M * 3.6
print(f'{M:.2f} m/s = {K:.2f} km/h')