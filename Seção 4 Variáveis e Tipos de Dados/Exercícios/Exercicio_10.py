"""
Leia uma velocidade em KM/H (Quilômetros por hora) e converta para M/S (Metros por segundo)

Formula:
K = Quilômetros
M = Metros
M=K/3.6
"""

K = float(input('Insira o valor em Quilômetros por hora : '))
M = (K / 3.6)
print(f'O valor convertido para metros por segundo é : {M}')
