"""
Elabore uma funlão que receba três notas de um aluno como parâmetro e uma letra.
Se a letra for A, a função devrá calcular a média aritmética das notas do aluno
se for P, deverá calcular a média ponderada, com pesos 5,3 e 2.
"""


def calc_media(notas, operacao):
    media = 0
    pesos = [5, 3, 2]
    notas_ponderadas = []
    contador = 0
    if operacao == 'A':
        media = sum(notas) / len(notas)
    elif operacao == 'P':
        for i in notas:
            notas_ponderadas.append(i * pesos[contador])
            contador += 1
        media = sum(notas_ponderadas) / sum(pesos)
    else:
        print('Operação selecionada Inválida')

    return media


lista_de_notas = []

while len(lista_de_notas) < 3:
    lista_de_notas.append(float(input(f'Informe a {len(lista_de_notas) + 1}° Nota: ')))
forma_de_calcular_media = input('Envie:'
                                '\n "A" para calcular a média aritmética das notas'
                                '\n "P" para calcular a média ponderada com pesos (5,3,2): \n')
print(f'Media das notas equivale: {calc_media(lista_de_notas, forma_de_calcular_media.upper())}')
