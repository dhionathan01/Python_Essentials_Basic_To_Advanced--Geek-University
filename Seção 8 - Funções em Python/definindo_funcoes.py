"""
Definindo Funções

 - Funções são pequenas partes de código que realizam tarefas específicas.
 - Pode ou não receber entradas de dados e retornar uma saída de dados.
 - Muito uteis para executar procedimentos similares por repetidas vezes.

OBS: Se você escrever uma função que realiza várias tarefas dentro dela
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras.

"""

'''
# Exemplo de utilização de funções:
cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando funções integradas do Python (Built-in) exemplo print()

print(cores)

curso = 'Programação em Python: Essencial'

print(curso)

cores.append('roxo')
print(cores)
'''
# curso.append('Mais dados...') # Atribute Erro a função append não pode ser usando em um elemento tipo string

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.

# Como definir funções ?
"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:
nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case).
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não.
bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ou não ter retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao python que estamos definindo
uma função. Também abrimos o bloco de código já conhecido como dois pontos: Que é utilziado em Python para definir
blocos.

"""


# Definindo a primeira função

def diz_oi():
    print('oi!')


"""

OBS: 

1 - Veja que, dentro das nossa funções podemos utilizar outras funções.
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz pe dizer oi;
3 - Veja que está função não recebe nennum parâmetro de entrada.
4 - Veja que está função não retorna nada.
"""

# Utilizando funções
# Chamando funão
# diz_oi()

"""
Atenção:

Nunca esqueça de utilziar o parênteses ao executar uma função.
Exemplo:

#ERRADO
diz_oi

#CERTO
diz_oi()

#ERRADO
diz_oi ()

"""

# Exemplo 2

# Definindo Função


def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')


# Chamando função:

'''
for n in range(5):
    cantar_parabens()
'''

# Em Python, podemos inclusive criar variáveis do tipo de função e executar esta função através da variável.
# OBS: Isso não é recomendado

canta = cantar_parabens

canta()
