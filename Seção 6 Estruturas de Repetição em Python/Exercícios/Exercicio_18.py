"""
Escreva um algortimo que leia certa quantidade de números e informa o maior deles
e quantas vezes o número foi lido ?
"""
qtd_numeros = int(input('Insira a quantidade de números a ser inserida: '))
lista_de_numeros = []
log_de_entradas = 1
while len(lista_de_numeros) < qtd_numeros:
    lista_de_numeros.append(int(input(f'Insira {log_de_entradas}° valor: ')))
    log_de_entradas += 1
maior = max(lista_de_numeros)
numero_ocorrencia = lista_de_numeros.count(maior)
print(f'Maior número inserido: {maior}')
print(f'número de ocorrênicas d maior número: {numero_ocorrencia}')
