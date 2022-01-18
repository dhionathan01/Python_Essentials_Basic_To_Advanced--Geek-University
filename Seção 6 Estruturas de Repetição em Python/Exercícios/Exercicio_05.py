""" Faça um programa que peça o usuário pra digitar 10 valores e some-os"""
total = 0
for i in range(1, 10+1):
    valor = float(input('Digite o valor {}/10 : ' .format(i)))
    total = total + valor

print(f'Soma dos valores digitado: {total}')