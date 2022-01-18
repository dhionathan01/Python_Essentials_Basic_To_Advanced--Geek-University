"""
Leia uma temperatura em Graus Fahrenheit e apresente-a convertida em graus  Celsius.
Formula:
C = Celius
F = Fahrenheint

C=5.0*(F-32.0)/9.0
"""
F = float(input("Insira o valor em Fahrenheint: "))
C = 5.0 * (F - 32.0) / 9.0
print(f'O valor em Graus Celsius equivale a : {C}')

