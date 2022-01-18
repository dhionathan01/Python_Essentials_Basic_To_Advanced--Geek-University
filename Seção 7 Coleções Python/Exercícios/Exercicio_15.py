"""
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminado elementos repetidos
"""
vetor = []
while len(vetor) < 20:
    valor = float(input(f'Insira o {len(vetor)+1}° Valor: '))
    vetor.append(valor)

print(f' Lista de Valore gerados: {vetor}')
print(f' Eliminando Valores repetidos: {set(vetor)}')