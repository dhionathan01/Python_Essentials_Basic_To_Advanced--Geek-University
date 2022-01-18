"""
Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmônica:
H(n) = 1 + 1/2 + 1/3 +1/4 + 1/5... 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n)
"""
n = int(input('Informe o valor chave da série harmônica: '))
contador = 1
resultado = 0
if n > 0:
    while contador < n:
        resultado += 1/contador
        contador += 1
else:
    print('Valor tem de ser positivo')
    exit()
print(f'Valor de H({n}) equivale: {resultado}')
