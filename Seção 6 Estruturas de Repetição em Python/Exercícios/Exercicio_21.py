"""
Faça um programa que recaba dois números. Calcule e mostre:
* A soma dos números pares desse intervalo de números, incluindo os valores digitados
* A multiplicação dos valores ímpares desse intervalo, incluindo os digitados
"""

num1 = int(input('Insira o número de inicialização: '))
num2 = int(input('Insira o número de encerramento: '))

soma_de_numeros_pares = 0
multiplicacao_dos_numeros_impares = 1

for valor in range(num1, num2+1):
    if valor % 2 == 0:
        soma_de_numeros_pares += valor

    else:
        multiplicacao_dos_numeros_impares *= valor

print(f'Soma de números Pares: {soma_de_numeros_pares}')
print(f'Multiplicação de números Impares: {multiplicacao_dos_numeros_impares}')
