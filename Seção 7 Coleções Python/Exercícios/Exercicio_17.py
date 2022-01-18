"""
Leia um vetor de 10 posições e atribua o valor 0 para todos os elementos que possuírem valor negativo
"""
vetor = []
contador = 1
while len(vetor) < 10:
    vetor.append(int(input(f'Informe o {contador}° valor de 10: ')))
    contador += 1

print(f'Lista de  Valores inseridos: \n{vetor}')
conversao = vetor.copy()
for i in range(len(conversao)):
    if conversao[i] < 0:
        conversao[i] = 0
print(f'Lista com valores negativos convertidos para 0: {conversao}')