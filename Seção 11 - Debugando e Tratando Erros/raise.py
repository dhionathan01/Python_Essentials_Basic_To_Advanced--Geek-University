"""
Levantando os próprios erros com raise

raise -> Lança excecções

OBS: O raise não é uma função. É uma plavra reservada, assim como def ou qualquer outra em python.

Para simplificar pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoError('Mensagem de erro')
"""

'''
# Exemplo 1

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} sera impresso na cor {cor}')


colore('Dhionathan', 4)
'''

'''
# Exemplo 2


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A Cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} sera impresso na cor {cor}')


colore('Dhionathan', 'preto')
OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
'''