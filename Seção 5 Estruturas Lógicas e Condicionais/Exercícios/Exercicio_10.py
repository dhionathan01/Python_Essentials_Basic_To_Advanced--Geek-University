"""
Faça um programa que recebe a altura eo sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes
fórmulas (onde h corresponde à altura):
- Homens: (72.7 * h) - 58
- Mulheres: (62,1 * h) - 44,7
"""
sexo = input('Digite o seu Sexo (Masculino) ou (Feminino): ')
sexo = sexo.title()
h = float(input('Digite sua altura em Metros: '))
print(f'Detalhes do Usuário: \n - Sexo: {sexo} \n - altura: {h}')
if sexo == 'masculino':
    peso_ideal = (72.7 * h) - 58
    print(f'Peso ideial: {peso_ideal:.2f}')
elif sexo == 'feminino':
    peso_ideal = (62.1 * h) - 44.7
    print(f'Peso ideal: {peso_ideal:.2f}')

else:
    print('Sexo ou altura inválido')
