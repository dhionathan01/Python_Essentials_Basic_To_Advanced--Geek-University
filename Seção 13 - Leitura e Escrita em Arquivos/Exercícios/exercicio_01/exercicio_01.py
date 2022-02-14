"""
Escreva um programa que:
1 - Crie/Abra um arquivo texto de nome "arq.txt"
2 - Permita que o usuário grave diversos caracteres nesse arquivo, ate que o usuário entre com o caracter '0'
3 - Feche o arquivo
"""
import os


def metodo_abertura():
    modo = None
    if os.path.exists('arq.txt'):
        modo = input('O arquivo já existe \n'
                     'Insira: 1 - Sobrescrever o conteúdo, 2 - Escrever nas linhas seguintes: ')
    else:
        modo = '1'

    if modo == '2':
        print('Contéudo anterior mantido')
        return 'a'
    else:
        print('Arquivo Será sobrescrito')
        return 'w'


def escrever_arquivo():
    with open('arq.txt', metodo_abertura(), encoding='utf-8') as arquivo:
        while True:
            storange_of_caracters = input('Digite os textos que deseja salvar: ')
            if storange_of_caracters == '0':
                break
            arquivo.write(f'{storange_of_caracters} \n')

    verificando_se_arquivo_foi_fechado(arquivo)


def ler_arquivo():

    with open('arq.txt', 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())

    verificando_se_arquivo_foi_fechado(arquivo)


def verificando_se_arquivo_foi_fechado(arq_fechado):
    if arq_fechado:
        print('O arquivo foi fechado corretamente')
    else:
        print('O arquivo está aberto ou não foi fechado corretamente')


choice = input('Insira: 1 - Para ler o arquivo, 2 - Para criar/abrir e escrever no arquivo, 3 - Script padrão: ')
if choice == '1':
    ler_arquivo()
elif choice == '2':
    escrever_arquivo()
elif choice == '3':
    escrever_arquivo()
    ler_arquivo()
else:
    print('Opção selecionada inválida, executando Script Padrão')
    escrever_arquivo()
    ler_arquivo()
