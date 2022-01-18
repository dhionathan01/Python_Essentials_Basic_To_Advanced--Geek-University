"""
Escreva um algoritmo que leia um número inteiro entre 100 e 999
e imprima na saída cada um dos algarismos que compõem o número
"""
N = input("Insira um valor entre 100 e 999: ")
valor_inteiro = int(N)
if 100 <= valor_inteiro <= 999:
    for indice, caracter in enumerate(N):
        print(caracter)

else:
    print("O valor inserido não está entre 100 e 900")
