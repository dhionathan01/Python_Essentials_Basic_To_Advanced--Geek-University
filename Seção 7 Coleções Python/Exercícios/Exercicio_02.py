"""
Crie um programa que leia 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
"""
lista = []

for i in range(1, 7):
    valores = int(input('Insira o {}° Valor: '.format(i)))
    lista.append(valores)

print(lista)