"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis Locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.


Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linaguagem de tipagem dinâmica. Isso significa que ao declararmos
uma variável, nós não colocamos o tipo de dado dela.
Este tipo é interferido ao atribuírmos o valor a ela.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

Exemplo em Python:
numero = 42
"""
numero = 42  # Variável global ( Ela existira em todo o código, pode ser chamada ou usada sempre).
print(numero)
print(type(numero))

if numero > 10:
    nova_variavel = numero + 10  # Váriavel Tipo Local ( Ela só existira no código, e só poderar ser usada ou chamada
    print(nova_variavel)         # se o programa entrar nas condições estabelecidas no if, e criar a variável.

print('Test de Existência de variável :', nova_variavel)






