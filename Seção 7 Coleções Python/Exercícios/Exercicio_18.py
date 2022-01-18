"""
Faça um programa que leia um vetor de 10 números. Leia um
número x. Conte os múltiplos de um número inteiro x num vetor
e mostre-os na tela.
"""
vetor = []
contador = 1
while len(vetor) < 10:
    vetor.append(float(input(f'Informe o {contador}° valor de 10:  ')))
    contador += 1
multiplicador = int(input('Insira o multiplicador'))
lista_de_multiplicados = []
for i in vetor:
    lista_de_multiplicados.append(i * multiplicador)
print(f'Lista de Número Inseridos:\n {vetor}')
print(f'Lista de valores Inseridos multiplicados por {multiplicador}:\n{lista_de_multiplicados}')
