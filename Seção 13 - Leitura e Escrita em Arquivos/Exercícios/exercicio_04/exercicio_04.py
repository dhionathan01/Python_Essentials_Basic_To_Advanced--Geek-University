"""
Faça um programa que recaba do usuário um arquivo texto e mostre na tela:
* Número de vogais
* Número de consoantes
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
    return contador_de_vogais


def contar_consoantes(arquivo_recebido):
    lista_de_consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                           'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    contador_de_consoantes = 0
    for consoante in lista_de_consoantes:
        # verificando consoantes que estão em caixa baixa
        contador_de_consoantes += arquivo_recebido.count(consoante.lower())
        # verificando consoantes que estão em caixa alta
        contador_de_consoantes += arquivo_recebido.count(consoante.upper())
    return contador_de_consoantes


if __name__ == '__main__':
    nome_arquivo = (input('Insira o nome / caminho do arquivo: '))
    if '.txt' not in nome_arquivo:
        nome_arquivo += '.txt'

    textos_recebidos = abrindo_arquivo(nome_arquivo)
    vogais_contadas = contar_vogais(textos_recebidos)
    consoantes_contadas = contar_consoantes(textos_recebidos)
    print(f'O arquivo:{nome_arquivo} contém:\n'
          f'Vogais:{vogais_contadas}\n'
          f'Consoantes: {consoantes_contadas}\n')

