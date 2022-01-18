"""
Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.
"""
valor = 3
total = 0
for i in range(1, 5+1):
    total = valor * i
    print(f'{valor} x {i} = {total}')
