"""
Faça um programa que some todos o números naturais abaixo de 1000 que são múltiplos de 3 ou 5:
"""
valor = 0
soma = 0
while valor < 1000:
    valor = float(input('Insira um valor, para cancelar digite um valor acima de mil: '))
    if valor % 3 == 0 or valor % 5 == 0:
        soma += valor

print(f'A soma dos valores inseridos que são múltiplos de 3 ou 5 equivale: {soma}')
