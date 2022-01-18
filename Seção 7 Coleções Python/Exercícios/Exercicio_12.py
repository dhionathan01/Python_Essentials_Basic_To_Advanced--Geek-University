"""
Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor
e a média dos valores.
"""

lista = []

while len(lista) < 5:
    valor = float(input(f'Insira o {len(lista)+1}° Valor: '))
    lista.append(valor)

print(f'Valores Inseridos : {lista}')
print(f'Maior Valor Inserido: {max(lista)}')
print(f'Menor valor Inserido : {min(lista)}')
print(f'Média dos Valores Inseridos: {sum(lista)/len(lista)}')