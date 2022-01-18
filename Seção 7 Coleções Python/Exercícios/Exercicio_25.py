"""
Faça um programa que preencha um vetor de tamanho 100 com os primeiros naturais que não são multiplos de 7
ou que terminam com 7.
"""
from random import randint


def verificar_algortimo_final_7(valor_de_entrada):
    valor_para_string = str(valor_de_entrada)
    valor_para_string = valor_para_string[::-1]
    if valor_para_string[0] == '7':
        return True
    else:
        return False


vetor = []
final_7 = True

while len(vetor) < 100:

    valor = randint(0, 10000)
    final_7 = verificar_algortimo_final_7(valor)
    if valor % 7 != 0:
        if not final_7:
            vetor.append(valor)

print(vetor)
