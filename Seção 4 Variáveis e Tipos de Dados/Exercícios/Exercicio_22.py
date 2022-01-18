"""
Leia um valor de comprimento em Jardas e apresente-o convertido em metros.
A fórmula de conversão é:
M = 0,91 * J, J o comprimento em jardas e M o comprimento em metros
"""

J = float(input('Informe o valor em Jardas: '))
M = 0.91 * J
print(f'{J} jardas equivale: {M}m')
