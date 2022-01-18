"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso.
Calcule o consumo em Km/l e escreva:

Consumo menor que 8Km/l mensagem:
Venda o carro!
Consumo entre 8 e 14Km/l mensagem:
Econômico !
Consumo maior 14Km/l mensagem:
Super Econômico !

"""

km = float(input('Informe a quilometragem percorrida: '))
litros = float(input('Informe quantos litros foram gastos: '))

km_l = km/litros
if km_l < 8:
    print(f'Quilometragem por litros: {km_l}\n'
          f'Venda o Carro !')
elif 8 < km_l <= 14:
    print(f'Quilometragem por litros: {km_l}\n'
          f'Ecônomico !')

else:
    print(f'Quilometragem por litros: {km_l}\n'
          f'Super Econômico !')
