"""
Faça uma Função que retorne o maior fator primo de um número
"""


def maior_fator_primo(valor):
    maior_primo = 0
    for possivel_primo in range(1, valor+1):
        contador_de_divisores = 0
        for verificar_primo in range(1, possivel_primo+1):
            if possivel_primo % verificar_primo == 0:
                contador_de_divisores += 1
        if contador_de_divisores == 2:
            if valor % possivel_primo == 0:
                if possivel_primo > maior_primo:
                    maior_primo = possivel_primo

    return maior_primo


num = int(input("Digite um número: "))
print(f'Maior fator primo: {maior_fator_primo(num)}')
