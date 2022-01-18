"""
Leia a idade eo tempo de serviço de um trabalhador e escreva se ele pode ou não se apostentar.
As condições para aposentadoria são:

* Ter pelo menos 65 anos
* Ou ter trabalhado pelo menos 30 anos
* Ou ter pelo menos 60 anos e trabalhado pelo menos 25.
"""
idade = int(input('Insira Idade: '))
tempo_de_servico = int(input('Tempo de serviço (em anos): '))
aposentar = None
if idade >= 65 or tempo_de_servico >= 30 or idade >= 60 and tempo_de_servico >= 25:
    aposentar = True
else:
    aposentar = False

if aposentar:
    print('Pode Aposentar')
else:
    print('Não pode Aposentar')
