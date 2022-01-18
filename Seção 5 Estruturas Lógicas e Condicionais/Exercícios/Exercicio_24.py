"""
Uma empresa vende o mesmo produto para quatro diferentes estados.
Cada estado possui uma taxa diferente de imposto sobre o produto
(MG 7%; SP 12%; RJ 15%; MS 8%;)
Faça um programa em que o usuário entre com o valor eo estado destino do produto
e o programa retorne o preço final do produto acrescido do imposto do estado
em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
"""
valor_produto = float(input('Digite o valor do produto: '))
local = input('Informe a sigla do Estado: ')
imposto = None
local = local.upper()
if local == 'MG':
    imposto = 0.07
elif local == 'SP':
    imposto = 0.12
elif local == 'RJ':
    imposto = 0.15
elif local == 'MS':
    imposto = 0.08
else:
    print('Local Invalido')
    quit()
total = valor_produto + (valor_produto * imposto)
print(f'Região: {local}\n Valor Padrão: {valor_produto} \n Valor com Imposto: {total}')
