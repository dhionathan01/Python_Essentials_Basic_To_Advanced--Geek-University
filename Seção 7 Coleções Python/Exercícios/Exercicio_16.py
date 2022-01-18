"""
Faça um Programa que leia um vetor de 5 Posições para números reias e, depois um código inteiro. Se o código for zero
finalize o programa; se for 1, mostre o vetor na ordem direta; se for 2, mostre o vetorr na ordem inversa.
caso o código for diferente de 1 e 2 escreva uma mensagem informando que o código é inválido.
"""

vetor = []

while len(vetor) < 5:
    valor = float(input(f'Insira o {len(vetor)+1}° valor: '))
    vetor.append(valor)
codigo = int(input(f'Digite o Código de Exibição: \n - 1 Ordem de Inserção / - 2 Ordem Inversa \n : '))
if codigo == 1:
    print(f' Lista Ordem de Inserção : {vetor}')
elif codigo == 2:
    print(f' Lista Ordem Inversa : {vetor[::-1]}')
