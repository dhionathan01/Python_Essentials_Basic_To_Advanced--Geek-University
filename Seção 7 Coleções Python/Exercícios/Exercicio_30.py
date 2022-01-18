"""
Faça um programa que leia dois vetores de 10 elementos.
Crie um vetor que seja a intersecção entre os 2 vetores anteriores,
Ou seja, que contém apenas números que estão em ambos vetores. Não deve conter números repetidos.
"""

vetor1 = []
vetor2 = []
while len(vetor1) < 10:
    vetor1.append(int(input(f'Insira o {len(vetor1)+1}° valor do Vetor 1: ')))

while len(vetor2) < 10:
    vetor2.append(int(input(f'Insira o {len(vetor2)+1}° valor do Vetor 2: ')))

vetor_de_interseccao = []
for valor in vetor1:
    if valor in vetor2:
        vetor_de_interseccao.append(valor)

print(f'Valores do vetor 1:\n {vetor1}')
print(f'Valores do vetor 2:\n {vetor2}')
print(f'Intersecção dos vetores 1 e 2:\n {vetor_de_interseccao}')

