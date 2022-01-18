"""
Faça um Programa que Leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela
"""
vetor = []
valores_iguais = []
numero_ocorrencia = []

while len(vetor) < 10:
    valor = float(input(f'Insira o {len(vetor)+1}° valor :'))
    vetor.append(valor)

for i in range(len(vetor)):
    if vetor.count(vetor[i]) > 1:
        valores_iguais.append(vetor[i])
        numero_ocorrencia.append(vetor.count(vetor[i]))

print(f'Lista de Valores Inseridos: {vetor}')
print(f'Valores iguais {valores_iguais}')

