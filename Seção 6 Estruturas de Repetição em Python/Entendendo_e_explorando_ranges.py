"""
Ranges:
- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor loops em for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

- Exemplo:
range(valor_de_parada)
OBS: valor_de_parada não inclusive (o contador starta em 0 por padrão, e acrescenta de 1 em 1 e pausa valor_final -1

Formas gerais:
"""
'''
# Forma 01:
for valor_inicio in range(11):  # -> Se não anteriomente um valor para variável valor_inicio, ela inicia em 0.
    print(valor_inicio)
'''
'''
# Forma 02:
# range(valor de partida, valor de parada -1) automaticamente sendo incrementado de 1 em 1.
for valor_inicio in range(3, 11):
    print(valor_inicio)
'''
'''
# Forma 03:
# range(valor de partida, valor de parada - 1, incremento especificado.
for valor_inicio in range(5, 51, 5):
    print(valor_inicio)
'''

# Forma 04: (Decrescente)
for valor_inicio in range(10, -1, -1):  # -> Vale ressaltar que o valor_de_parada -1 ainda prevalece.
    print(valor_inicio)
