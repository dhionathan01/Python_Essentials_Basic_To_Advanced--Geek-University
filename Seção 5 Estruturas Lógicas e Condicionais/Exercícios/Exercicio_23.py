"""
Determine se um ano é bissexto.
Para um ano ser bissexto ele precisa ser divisível por 400 ou se for divísvel por 4 e não for divisível por 100.
Por exemplo:
1988, 1992, 1996...
"""
ano = int(input('Digite o ano: '))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('Ano correspondente é bissexto')
else:
    print('Ano correspondente não é bissexto')
