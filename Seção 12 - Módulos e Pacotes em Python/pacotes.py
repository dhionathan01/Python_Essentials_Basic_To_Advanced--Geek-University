"""
Pacotes
Módulo → É apenas um arquvi Python que pode ter diversas funções para utilizarmos.

Pacote → é um diretório contendo uma coleção de módulos.

OBS: Nas versões 2.x Python, um pacote Python deveria conter dentro dele
um arquivo chamado __init__.py

Nas versões do python 3.x, não é mais obrigatória a utilização deste arquivo, mas
normalmente ainda é utilizado para manter compatibilidade
"""

from Aprendendo_Pacotes import modulo_p_1, modulo_p_2   # importanto pacotes
from Aprendendo_Pacotes.Subpacote import modulo_sub_1, modulo_sub_2     # Importanto subpacotes

#   Usando modulo 1 do pacote principal
print(modulo_p_1.pi)
print(modulo_p_1.funcao1(4, 6))
#   Usando modulo 2 do pacote principal
print(modulo_p_2.curso)
print(modulo_p_2.funcao2())
#   Usando Subpacotes do pacote principal
print(modulo_sub_1.funcao3())
print(modulo_sub_2.funcao4())
