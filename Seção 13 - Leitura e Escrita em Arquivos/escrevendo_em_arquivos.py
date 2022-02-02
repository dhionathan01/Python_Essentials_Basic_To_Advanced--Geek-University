"""
Escrevendo em arquivos


# OBS: Ao abrir um arquivo para leitua, não podemos realizar a escrita nele. Apenas ler
De forma semelhante, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError

# Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir erá criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, qualquer
conteúdo no arquivo anterior é perdido.
"""

# Exemplo de escrita - modo 'w' - write (escrita) - Não Forma Pythonica

arquivo = open('novo_nao_pythonico.txt', 'w', encoding='utf-8')
arquivo.write('Um texto qualquer. \n')
arquivo.write('Mais um texto.')
arquivo.close()

# Exemplo de escrita - modo 'w' - write (escrita) - Forma Pythonica

with open('novo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros podemos colocar quantas linha quisermos\n')
    arquivo.write('Está é a útima linha.\n')

# Exemplo Pegando dados do usuário e colocando em um arquivo

with open('frutas.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe uma forta ou digite sair: ')
        if fruta.title() != 'Sair':
            arquivo.write(f'{fruta} \n')
        else:
            break
