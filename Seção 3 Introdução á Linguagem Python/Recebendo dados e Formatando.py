"""
Recebendo dados do usuário.
input() -> Todo dado recebido via input é do tipo string.
Em python, string é tudo que estiver entre:
- Aspas Simples.
- Aspas Duplas.
- Aspas Simples triplas.
- Aspas duplas triplas.

Exemplos :
- Aspas Simples -> 'Dhionathan Jobim'
- Aspas Duplas -> "Dhionathan Jobim"
- Aspas Simples Triplas -> '''Dhionathan Jobim'''
"""
# - Aspas Duplas Triplas -> """Dhionathan Jobim"""

# Entrada de dados
# print("Qual seu nome ?")
# nome = input()  # Input Entrada
# Preencher váriavel como texto de exibição
nome = input('Qual seu nome ? ')

# Exemplo de Print Python versão 2.x
# print('Seja bem-vindo(a) %s' %nome)

# Exemplo Print 'moderno' Python versão 3.x
# print('Seja bem-vindo(a){0}' .format(nome))

# Print 'mais atual' 3.8
print(f'Seja bem vindo (a) {nome}')
# print("Qual sua idade ?")
# idade = input()
# Preencher váriavel como texto de exibição
idade = input('Qual sua idade ? ')

# Processamento

# Saída
# Exemplo de Print Python versão 2.x
# print('%s tem %s anos' % (nome, idade))

# Exemplo Print 'moderno' Python versão 3.x
# print('{0} tem {1} anos' .format(nome, idade))

# Exemplo Print mais atual Python versão 3.8
print(f'{nome} tem {idade} anos')

"""
# int(idade) => cast
Cast é a 'conversão' de um tipo de dado pra outro.
"""
print(f'{nome} nasceu em {2020 - int(idade)}')
