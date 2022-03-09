"""
Faça um prorama que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo,
mas com todas as letras minúsculas convertidas para maiúsculas.
Os nomes dos arquivos serão forneceidos, via teclado, pelo usuário.
"""
import sys
import os.path


def abrir_arquivo():
    nome = None
    arquivo_exist = os.path.exists(f'{nome}')
    while not arquivo_exist:
        nome = input('Insira o nome do arquivo: ')
        if '.txt' not in nome:
            nome += '.txt'
        arquivo_exist = os.path.exists(f'{nome}')

        if not arquivo_exist:
            print('Arquivo Não encontrado')
            again = input('Deseja tentar abrir outro arquivo ? s / n')
            if again.lower() == 's':
                pass
            elif again.lower() == 'n':
                print('Arquivo Encerrado')
                sys.exit()
            else:
                print('Opção inválida')

    try:

        with open(nome, 'r', encoding='utf-8') as arquivo:
            conteudo_arq = arquivo.read()
            return conteudo_arq
    except FileNotFoundError:
        print('Arquivo Não encontrado')
    except OSError:
        print('O nome do arquivo não pode conter caracteres especiais')


def escrevendo_arquivo(conteudo):
    nome = input('Insira o nome do arquivo que deseja criar: ')
    if '.txt' not in nome:
        nome += '.txt'
    arquivo_exist = os.path.exists(f'{nome}')
    if arquivo_exist:
        print('Arquivo Já existe')
        nome = input('Insira outro nome:')
        if '.txt' not in nome:
            nome += '.txt'

    with open(nome, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
        print(f'As modificações foram salvas no arquivo {nome}')


def alterando_letras(conteudo):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letra in letras:
        conteudo = conteudo.replace(letra, letra.upper())
    return conteudo


if __name__ == '__main__':
    conteudo_recebido = abrir_arquivo()
    conteudo_modificado = alterando_letras(conteudo_recebido)
    escrevendo_arquivo(conteudo_modificado)
