"""
Len, Abs, Sum, Round

# Len() -> Retorna o tamanho o tamanho (ou seja, o número de itens) de um iterável.

"""
'''
# Revisão
print(len('Dhionathan Jobim'))
print(len([1, 2, 3, 4, 5]))
print(len({1, 2, 3, 4, 5}))
print(len((1, 2, 3, 4, 5)))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}))
print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len 
print('Dhionathan Jobim'.__len__())
'''

'''
# abs() -> Retorna o valor absoluto de um númeiro inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

print(abs(5))
print(abs(-5))
print(abs(3.14))
print(abs(-3.14))
'''
'''
# Sum 
sum() -> Recebe como parâmetro um iterável , Podemos receber um valor inicial, e retornar a somta total dos elementos,
incluindo o valor inicial defaul = 0


print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.145, 5.678]))

print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))
'''

'''
# Round

round() -> Retorna um número arredondado para n digito de precisão após a casa decima. Se a precisão naõ for informada
retorna o inteiro mais próximo da entrada
'''

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.21212121, 2))
print(round(1.2199999, 2))
