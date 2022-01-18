"""
Faça uma função que recaba distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso.

Calcule o consumo em Km/l e escreva:
Consumo menor que 8Km/l mensagem:
Venda o carro!
Consumo entre 8 e 14Km/l mensagem:
Econômico !
Consumo maior 14Km/l mensagem:
Super Econômico !
"""


def calcula_km_p_litros(quilometros, litros_consumidos):
    km_l = quilometros / litros_consumidos
    if km_l < 8:
        print(f'Quilometragem por litros: {km_l}\n'
              f'Venda o Carro !')
    elif 8 < km_l <= 14:
        print(f'Quilometragem por litros: {km_l}\n'
              f'Ecônomico !')

    else:
        print(f'Quilometragem por litros: {km_l}\n'
              f'Super Econômico !')


km = float(input('Quilometragem percorrida: '))
litros = float(input('Litros gastos: '))
calcula_km_p_litros(km, litros)
