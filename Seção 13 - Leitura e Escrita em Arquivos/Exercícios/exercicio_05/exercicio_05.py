"""
Faça um programa que receba do usuário um arquivo texto e um caracter.
Mostre na tela quantas vezes aquele caracter ocorre dentro do arquivo:
"""
import sys


def abrindo_arquivo(nome):
    try:
        with open(nome, 'r', encoding='utf-8') as arquivo:
            arquivo = arquivo.read()
            return arquivo
    except FileExistsError:
        print('Arquivo não existe')
        sys.exit()
    except FileNotFoundError:
        print('Arquivo não encontrado')
        sys.exit()
    except OSError:
        print('O nome do arquivo não pode conter caracter especial')
        sys.exit()


def contar_ocorrencia(arquivo_recebido, caracter_escolhido):
    try:
        contador = arquivo_recebido.count(caracter_escolhido)
        return contador
    except AttributeError:
        print('Não foi possivel efetuar a contagem')
        sys.exit()


if __name__ == '__main__':

    nome_do_arquivo = input('Insira o nome do arquivo: ')
    if '.txt' not in nome_do_arquivo:
        nome_do_arquivo += '.txt'

    dados_do_arquivo = abrindo_arquivo(nome_do_arquivo)
    caracter = input('Insira o caracter que deseja contar as ocorrências no arquivo: ')
    numero_de_ocorrencia = contar_ocorrencia(dados_do_arquivo, caracter)

    print(f' Dentro do arquivo: {nome_do_arquivo}\n Foram encontrados {numero_de_ocorrencia} caracters "{caracter}"')
