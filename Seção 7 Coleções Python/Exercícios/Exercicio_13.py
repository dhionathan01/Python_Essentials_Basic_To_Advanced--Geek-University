"""
Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior eo menor valor.
"""
vetor = []

while len(vetor) < 5:
    valor = float(input(f'Insira o {len(vetor)+1}° Valor: '))
    vetor.append(valor)

print(f'Lista de Valores Inseridos: {vetor}')
print(f' Maior Valor Inserido: {max(vetor)} / Ocupa a Índice {vetor.index(max(vetor))}')
print(f' Menor valor Inserido: {min(vetor)} / Ocupa o Índice {vetor.index(min(vetor))}')