"""
Leia um valor de área em jardas e apresente-o convetido em metros quadrados. A fórmula de conversão é:
M = A * 4 048,58, sendo M a área em metros quadrados e 'A' a área em acres
"""
A = float(input('Informe o valor em Acres: '))
M = A * 4048.58
print(f'{A} acres equivale: {M} metros')
