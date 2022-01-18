"""
Módulo Random e o que são módulos ?
- Em python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.
"""

# OBS: Existem duas forma de se utilizar um módulo ou função deste

# Forma 1 : Importando todo o módulo (Não recomendado).

# import random

# random() -> Gera um número pseudo-aleatório entre 0 e 1.
"""
 Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem dentro do
módulo  ficarão disponíveis (ficarão em Memória). Caso você saiba quais funções você precisa utilziar deste módulo,
então esta não seria a forma idela de utilização. Nós veremos uma forma melhor na forma 2.
"""
# print(random.random())
# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e eo nome da função,
# separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confunso, mas a função random() é apenas uma
# Função dentro do módulo random.

# Forma 2 - Importando uma função específica do módulo random (Forma recomendada)

'''
from random import random

# No import acim estamos falando: Dó módulo random, importe a função random

for i in range(10):
    print(random())
'''

'''
# uniform() -> Gera um número real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(5, 10))    # o 10 Não é incluído.
'''

'''
# randint() -> Gera valores interios pseudo aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')     # começa em 1 e vai até 60
'''
'''
# choice() -> Mostra um valor aleatório entre um iterável
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
print(choice(Dhionathan Jobim))
'''

# shuffle() -> Tem a função de embaralhar dados
from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)

shuffle(cartas)

print(cartas)
