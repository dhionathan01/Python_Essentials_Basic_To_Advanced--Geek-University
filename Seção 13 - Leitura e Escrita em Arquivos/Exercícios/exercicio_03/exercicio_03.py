"""
Faça um programa que recaba do usuário um arquivo texto e mostre na tela quantas letras são vogais.
"""
try:
    nome_arquivo = (input('Insira o nome / caminho do arquivo: '))
    if '.txt' not in nome_arquivo:
        nome_arquivo += '.txt'

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        contador_de_vogais = 0
        arquivo = arquivo.read()
        lista_de_vogais = ['a', 'e', 'i', 'o', 'u']
        for vogal in lista_de_vogais:
            contador_de_vogais += arquivo.count(vogal.lower())  # verificando vogais que estão em caixa baixa
            contador_de_vogais += arquivo.count(vogal.upper())  # verificando vogais que estão em caixa alta
        print(contador_de_vogais)

except FileExistsError:
    print('\n Arquivo não existe')
except FileNotFoundError:
    print('\n Arquivo não foi encontrado')
except OSError:
    print(' \nNomes de arquivos não podem conter caracteres especiais')

