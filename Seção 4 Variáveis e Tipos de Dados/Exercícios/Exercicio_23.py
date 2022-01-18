"""
Leia um valor de comprimento em metros e apresente-o convertido em jardas.
A fórmula de conversão é:
J = 0.91 / M, sendo J o comprimento em jardas e M o comprimento em metros
"""

M = float(input('Informe o valor em Jardas: '))
J = M / 0.91
print(f'{M}m equivale: {J} jardas')
