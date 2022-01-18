"""
Módulos Externos
Utilizamos o gerenciador de pcaotes Python Chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

Colorama -> É utilizado para permitir impressão de textos coloridos no terminal

Instalando módulos externos em Python:
pip install nome-do-modulo
exemplo:
pip install colorama
"""
'''
from colorama import init, Fore, Back, Style
init()
print(Fore.RED + 'Dhionathan Jobim')
print(Fore.GREEN + 'Dhionathan Jobim')
print(Fore.YELLOW + 'Dhionathan Jobim')
print(Fore.BLUE + 'Dhionathan Jobim')
print(Fore.LIGHTBLUE_EX + 'Dhionathan Jobim')
'''

import pydf
pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

