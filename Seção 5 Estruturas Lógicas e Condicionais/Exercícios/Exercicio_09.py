"""
Leia o Salário de um trabalhador e o valor da prestação de um emprestio. Se a prestação for maior que 20% do salário
imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
"""

salario = float(input('Insira o Salário do Trabalhador: '))
prestacao = float(input('Insira o valor da Prestação: '))
emprestimo = False
validar = (salario / 100) * 20

if validar > prestacao:
    emprestimo = True

else:
    emprestimo = False

if emprestimo is True:
    print('Empréstimo Concedido')
else:
    print('Empréstimo não concedido')

