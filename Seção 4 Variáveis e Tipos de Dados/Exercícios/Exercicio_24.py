"""
Leia um valor de área em metros quadrados e apresente-o convetido em acres. A fórmula de conversão é:
A = M * 0, 000 247, sendo M a área em metros quadrados e 'A' a área em acres
"""
M = float(input('Informe o valor em metros quadrados: '))
A = M * 0.000247
print(f'{M}m equivale: {A} acres')
