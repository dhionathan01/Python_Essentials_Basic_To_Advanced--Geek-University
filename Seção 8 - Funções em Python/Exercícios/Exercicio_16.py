"""
Faça uma fução chamada DesenhaLinha. Ela deve senhar uma linha na tela usando vários símbolos de igual
EX: ===============
A função recebe por parâmetro quantos sinais de igual serão mostrados
"""


def DesenhaLinha(quantidade):
    linha = ''
    for i in range(quantidade):
        linha += '='

    print(linha)


valor = int(input('Informe o valor da linha: '))
DesenhaLinha(quantidade=valor)
