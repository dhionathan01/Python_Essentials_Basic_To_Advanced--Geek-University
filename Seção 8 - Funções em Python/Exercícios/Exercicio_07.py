"""
Faça uma função que recaba uma temperatura em graus celsius e retorne-a convertida em graus fahrenheit.
A fórmula de conversão é F = C x (9,0/5,0) _ 32,0
Sendo F a temperatura em Fahrenheit e C a temperatura em celius.
"""


def converter_Celsius_Fahrenheit(C):
    F = C * (9.0 / 5.0) + 32.0
    return F


C = float(input('Informe a temperatura em Celsius: '))
print(f'A temperatura em Fahrenheit equivale: {converter_Celsius_Fahrenheit(C)}')
