"""
Leia uma distância em quilômetros e aprensente-a convertida em milhas. A fóruma de conversão é : M = K/1,61
send K a distância em quilômetros e M em milhas.
"""

K = float(input('Digite o Valor em Km: '))
M = K/1.61
print(f'{K} Km convertido para milhas equivale: {M:.2f} milhas')
