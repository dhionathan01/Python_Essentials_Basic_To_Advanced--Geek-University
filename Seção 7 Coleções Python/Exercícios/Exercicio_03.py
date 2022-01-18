"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando
o resultado em outro vetor. os conjuntos tem 10 elementos cada. Imprimir todos os conjuntos.
"""
import random

numeros = []
numeros_quadrados = []
for i in range(10):
    valor = random.randrange(0, 1000)  # Gerando números Aleatórios para preencher o vetor.
    numeros.append(valor)
    numeros_quadrados.append(numeros[i]**2)
print(f'Lista de Números:\n {numeros}')
print(f'Quadrado dos Números:\n {numeros_quadrados}')
