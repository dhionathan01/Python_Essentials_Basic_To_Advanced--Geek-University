"""
Ler um Número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido". Se o número for positivo,
calcular o logaritmo deste numero.
"""
import math
numero = float(input("Insira o número que deseja calcular o Log: "))
total = math.log10(numero)
print(f'Log de {numero} = {total:.2f}')
