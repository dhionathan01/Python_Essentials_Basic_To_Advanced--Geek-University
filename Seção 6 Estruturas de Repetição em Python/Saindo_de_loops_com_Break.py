"""
Saindo de loops com break

Funciona da mesma forma que nas linguagens C ou Java.

Utilizamos o break para sair de loops de maneira projetada.
"""

# Exemplo 01

for numero in range (1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')

# Exemplo 02:

while True:
    resposta = input('Digite sair, para finalizar o loop: ')
    resposta = resposta.lower()
    if resposta == 'sair':
        break
