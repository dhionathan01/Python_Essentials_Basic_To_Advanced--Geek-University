"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido
"""
valores = []
for i in range(1, 11):
    valor = int(input('Digite o {}° número: '.format(i)))
    valores.append(valor)

print(f'Valores Inseridos: {valores}')
print(f'Maior Valor Inserido: {max(valores)}')
print(f'Menor Valor Inserido: {min(valores)}')
