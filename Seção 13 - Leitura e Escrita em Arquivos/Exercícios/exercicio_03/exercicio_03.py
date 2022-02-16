"""
Faça um programa que recaba do usuário um arquivo texto e mostre na tela quantas letras são vogais.
"""


def abrindo_arquivo(nome):
    try:
        with open(nome, 'r', encoding='utf-8') as arquivo:
            arquivo = arquivo.read()
            return arquivo

    except FileExistsError:
        print('\n Arquivo não existe')
    except FileNotFoundError:
        print('\n Arquivo não foi encontrado')
    except OSError:
        print(' \nNomes de arquivos não podem conter caracteres especiais')


def contar_vogais(arquivo_recebido):
    lista_de_vogais = ['a', 'e', 'i', 'o', 'u']
    contador_de_vogais = 0
    for vogal in lista_de_vogais:
        contador_de_vogais += arquivo_recebido.count(vogal.lower())  # verificando vogais que estão em caixa baixa
        contador_de_vogais += arquivo_recebido.count(vogal.upper())  # verificando vogais que estão em caixa alta
    print(contador_de_vogais)


if __name__ == '__main__':
    nome_arquivo = (input('Insira o nome / caminho do arquivo: '))
    if '.txt' not in nome_arquivo:
        nome_arquivo += '.txt'

    textos_recebidos = abrindo_arquivo(nome_arquivo)
    contar_vogais(textos_recebidos)

