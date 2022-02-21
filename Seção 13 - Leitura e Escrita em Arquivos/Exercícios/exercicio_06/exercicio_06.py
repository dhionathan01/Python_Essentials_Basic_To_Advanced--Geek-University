"""
Faça um programa que receba do usuário um arquivo texto
e mostre na tela quantas vezes cada letra do alfabeto aparece dentro do arquivo
"""
import sys


def abrir_arquivo(nome):
    try:
        with open(nome, 'r', encoding='utf-8') as arquivo:
            dados_do_arquivo = arquivo.read()
            return dados_do_arquivo
    except FileNotFoundError:
        print('Arquivo não encontrado')
        sys.exit()
    except FileExistsError:
        print('Arquivo não existe')
        sys.exit()
    except OSError:
        print('O nome do arquivo não pode conter caracteres especiais')
        sys.exit()


def contar_letras(arquivo):
    lista_de_contagem = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lista_contada = []
    lista_de_dados = []
    for letra in lista_de_contagem:
        contador = arquivo.count(letra)
        lista_contada.append(letra)
        lista_contada.append(contador)
        lista_de_dados.append([lista_contada.pop(), lista_contada.pop()])
    return lista_de_dados


def exibicao_encadeada(lista_de_dados):
    for dado in lista_de_dados:
        print(f'Letra: {dado[1]} ocorrências: {dado[0]}')


if __name__ == '__main__':
    nome_do_arquivo = input('Insira o nome do arquivo: ')
    if '.txt' not in nome_do_arquivo:
        nome_do_arquivo += '.txt'

    dados = abrir_arquivo(nome_do_arquivo)
    lista = contar_letras(dados)
    exibicao_encadeada(lista)
