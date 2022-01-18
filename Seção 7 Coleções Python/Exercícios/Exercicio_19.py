"""
Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i+5*i)%(i+1).
Sendo i a posição do elemento no vetor, em seguida printe o vetor na tela
"""
vetor = []
for i in range(50):
    vetor.append((i + 5 * i) % (i + 1))
print(f'Exibição de Lista: {vetor}')
