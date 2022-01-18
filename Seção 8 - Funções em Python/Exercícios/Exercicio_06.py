"""
Faça uma função que receba 3 números inteiros como parâmetro
representando horas, minutos e segundos e os converta em segundos
"""


def convSegundos(hora, minutos, segundos):
    hora_convertida_segundos = (hora * 60) * 60
    minutos_convertido_segundos = minutos * 60
    valor_convertido = hora_convertida_segundos + minutos_convertido_segundos + segundos
    return valor_convertido


h = int(input('Informe as Hora: '))
m = int(input('Informe os minutos: '))
s = int(input('Informe os segundos: '))
print(f'Valor convertido equivale: {convSegundos(h, m, s)}s')
