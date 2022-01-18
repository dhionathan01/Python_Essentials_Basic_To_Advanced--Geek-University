"""
Faça uma funcão que receba a data atual ( dia, mês  e ano em inteiro) e exiba=a na tela no formato textual por extenso.
Exemplo: data: 01/01/2000, imprimir: 1 janeiro de 2000.
"""


def converter_data(day, month, years):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril',
             'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
             'Outubro', 'Novembro', 'Dezembro']
    print(f'{day} de {meses[month-1]} do ano {years}')


data = [int(input('Insira o Dia: ')), int(input('Insira o Mês: ')), int(input('Insira o Ano: '))]
dia, mes, ano = 0, 1, 2
if 0 < data[dia] <= 31 and 0 < data[mes] <= 12 and data[ano] > 0:
    converter_data(data[0], data[1], data[2])
else:
    print('Data informada não é válida')
