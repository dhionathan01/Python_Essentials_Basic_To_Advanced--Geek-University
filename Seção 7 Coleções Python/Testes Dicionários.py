# adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

indice = True

while indice:
    print('Digite o indíce a ser  Adicionado ou -1 para cancelar a operação')
    indice = input('Digite o indíce : ')
    if indice == '-1':
        break
    valor = float(input('Digite o valor:'))
    novo_dado = {f'{indice}': valor}
    receita.update(novo_dado)

print(receita)
