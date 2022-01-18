"""
Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.

"""
soma = 0
numeros = 10
for i in range(1, 11):
    valor = int(input('Digite o {}° valor: '.format(i)))
    if valor >= 1:
        soma = soma + valor
    else:
        numeros = numeros - 1

total = soma/numeros
print(f'Resultado: {total}')
