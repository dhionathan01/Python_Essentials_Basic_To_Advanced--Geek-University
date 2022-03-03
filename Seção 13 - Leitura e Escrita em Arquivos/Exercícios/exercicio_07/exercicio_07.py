"""
Faça um programa que receba do usuário um arquivo texto.
Crie um outro arquivo texto contendo o texto do arquivo de entrada, mas com vogais substituídas por '*'
"""


def abrir_documento(nome_doc):
    try:
        if '.txt' not in nome_doc:
            nome_doc += '.txt'
        with open(nome_doc, 'r', encoding='utf-8') as documento:
            conteudo_doc = documento.read()
        return conteudo_doc
    except FileNotFoundError:
        print('Não foi possível Encontrar o arquivo')
    except OSError:
        print('O nome do documento não pode onter caracters especiais')


def criar_novo_documento(nome_origem):
    try:
        nome_origem = nome_origem.replace('.txt', '')
        nome_documento_novo = nome_origem + 'formatado'
        if '.txt' not in nome_documento_novo:
            nome_documento_novo += '.txt'
        with open(nome_documento_novo, 'w', encoding='utf-8'):
            return nome_documento_novo
    except OSError:
        print('O nome do documento não pode onter caracters especiais')


def escrevendo_arquivo(nome_documento_es, texto):
    try:

        nome_documento_novo = nome_documento_es.replace('.txt', '')
        if '.txt' not in nome_documento_novo:
            nome_documento_novo += '.txt'
        with open(nome_documento_novo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto)
    except OSError:
        print('O nome do documento não pode onter caracters especiais')


def substitui_vogais(texto):
    letras = ['a', 'e', 'i', 'o', 'u']
    for letra in letras:
        texto = texto.replace(letra, '*')
        texto = texto.replace(letra.upper(), '*')
    return texto


if __name__ == '__main__':
    nome_documento = input('Informe o nome do documento: ')
    textos = abrir_documento(nome_documento)
    print(textos)
    novo_arq = criar_novo_documento(nome_documento)
    textos_formatados = substitui_vogais(textos)
    escrevendo_arquivo(novo_arq, textos_formatados)

