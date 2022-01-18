"""
Faça um programa que leia 10 números inteiros e imrpima sua média.
"""
soma = 0
for i in range(1, 11):
    valor = int(input('Digite o {}° número : '.format(i)))
    soma = soma + valor
total = soma/10
print(f'Resultado: {total}')
