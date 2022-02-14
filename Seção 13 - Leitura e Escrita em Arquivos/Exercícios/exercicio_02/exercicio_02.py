"""
Faça um programa que recabe do usuário um arquivo texto e mostre na tela quantas linhas esse arquivo Possui.
"""
import os
nome_arquivo = input('Insira o nome do arquivo txt que deseja saber o número de linha: ')
if os.path.exists(f'{nome_arquivo}.txt'):
    with open(f'{nome_arquivo}.txt', 'r', encoding='utf-8') as arquivo:
        numero_de_linhas = len(arquivo.readlines())
else:
    print('O arquivo informado não foi encontrado')

print(f'O arquivo possui:{numero_de_linhas}')
