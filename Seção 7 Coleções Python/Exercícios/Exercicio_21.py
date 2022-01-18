"""
Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada.
Crie um novo vetor denominado C calculando C = A - B.
Mostre na tela os dados do vetor C.
"""
A = []
B = []
C = []
contador = 1
while len(A) < 10:
    A.append(int(input(f'Insira o valor {contador}/10 do vetor A: ')))
    contador += 1
contador = 1
while len(B) < 10:
    B.append(int(input(f'Insira o valor {contador}/10 do vetor B: ')))
    contador += 1

for i in range(len(A)):
    C.append(A[i] - B[i])

for i in range(len(C)):
    print(f'{A[i]} - {B[i]} = {C[i]}')
