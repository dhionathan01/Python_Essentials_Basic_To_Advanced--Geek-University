"""
Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles.
Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos eo produto escalar, sendo o prudto
Esalar dado por: x1 * y1 + x2 * y2 + ... xn * yn
"""
x = []
y = []
produto = []
for i in range(5):
    x.append(int(input(f'Insira o valor {i+1}: ')))

for i in range(5):
    y.append(int(input(f'Insira o valor {i+1}: ')))

for i in range(5):
    produto.append(x[i]*y[i])
print(f'Conjunto 1: {x}')
print(f'Conjunto 2: {y}')
print(f'Conjunto produto unitário: {produto}')
print(f'Produto escalar: {sum(produto)}')
