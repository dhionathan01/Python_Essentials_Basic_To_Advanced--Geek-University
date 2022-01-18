"""
Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar os seguintes
passos:
    * (Parte 1) Atribua os seguintes valores a esse vetor: 1,0,5,-2,-5,7.
    * (Parte 2) Armazene em uma variável inteira (Simples) a soma entre os valores das posições A[0] , A[1], A[5] do
    vetor e mostre na tela esta soma.
    * (Parte 3) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
    * (Parte 4) Mostre na tela cada valor do vetor A, um em cada linha.
"""
A = []
A.extend([1, 0, 5, -2, -5, 7])  # Parte 1
print(A)

soma = A[0] + A[1] + A[5]   # Parte 2
print(f'Soma dos Vetores A[0] , A[1], A[5]: {soma}')    # Parte 2.1
A[4] = 100  # Parte 3
for i in range(len(A)):  # Parte 4
    print(A[i])
