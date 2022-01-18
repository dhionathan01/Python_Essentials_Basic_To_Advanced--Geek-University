"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
categoria ---------- idade
infantil A -------- 5 a 7
infantil B -------- 8 a 10
Juvenil A --------- 11 a 13
Juvenil B --------- 14 a 17
Sênior ------------- 18+
"""
idade = int(input('Informe a idade: '))
if 5 <= idade <= 7:
    print('Infantil A')
elif 8 <= idade <= 10:
    print('Infatil B')
elif 11 <= idade <= 13:
    print('Juvenil A')
elif 14 <= idade <= 17:
    print('Juvenil B')
elif idade >= 18:
    print('Sênior')
else:
    print('Idade não apta para classificação')