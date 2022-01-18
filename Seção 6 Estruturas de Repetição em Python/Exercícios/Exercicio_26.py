"""
Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após o número dado.
"""

valor = int(input('Informe o número: '))
verificador = valor
stop = False
while not stop:
    if verificador % 11 == 0:
        print(f'Múltiplo de 11 detectado')
        break
    elif verificador % 13 == 0:
        print(f'Múltiplo de 13 detectado')
        break
    elif verificador % 17 == 0:
        print(f'Múltiplo de 17 detectado')
        break
    verificador += 1

print(f'O valor mais próximo após {valor} que é múltiplo de 11, 13 ou 17: {verificador}')

