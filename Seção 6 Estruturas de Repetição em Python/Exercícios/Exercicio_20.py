"""
Ler uma sequência de números inteiros e determinar se eles são pares ou não.
Deverá ser infromado o número de dados lidos, e números de valores pares.
O processo termina quando for digitado o número 1000.
"""
valor = 0
entrada_de_dados = 0
qtd_numeros_pares_inseridos = 0
while valor != 100:
    entrada_de_dados += 1
    valor = int(input(f'Insira o {entrada_de_dados}° valor: '))
    if valor % 2 == 0:
        qtd_numeros_pares_inseridos += 1
entrada_de_dados -= 1   # Temos que remover o número 100 da contagem
qtd_numeros_pares_inseridos -= 1    # Temos que remover o número 100 da contagem
print(f'Quantidade de valores inseridos: {entrada_de_dados}\n'
      f'Quantidade de valores pares detectados: {qtd_numeros_pares_inseridos}')
