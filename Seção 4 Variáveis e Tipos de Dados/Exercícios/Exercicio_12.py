"""
Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão é:
K = quilômetros
M = milhas.
K = 1,61 * M
"""
M = float(input("Digite o valor em Milhas: "))
K = 1.61 * M
print(f'{M:.2f} milhas = {K:.2f} km')
