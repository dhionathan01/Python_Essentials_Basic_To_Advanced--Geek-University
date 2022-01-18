"""
Faça uma função que recaba dois números inteiros positivos por parâmetro e retorne a soma dos 'N' números inteiros
existetnes entre eles
"""


def soma_intercalada(inicio, fim):
    soma = 0
    for i in range(inicio, fim+1):
        soma += i
        print(i)
    return soma


valor_inicio = int(input('Informe o valor de início: '))
valor_fim = int(input('Informe o valor fim: '))

total = soma_intercalada(inicio=valor_inicio, fim=valor_fim)
print(f'A soma dos números no intervalo de {valor_inicio} a {valor_fim} equivale: {total}')
