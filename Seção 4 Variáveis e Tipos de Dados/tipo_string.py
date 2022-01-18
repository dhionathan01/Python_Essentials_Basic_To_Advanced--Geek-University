"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre aspas simples -> 'uma string', '123', 'a', 'true', '42.3'
- Estiver entre aspas duplas -> "uma string", "123", "a", "true", "42.3"
- Estiver entre aspas triplas -> '''uma string''', '''123''', '''a''', '''true''', '''42.3'''
"""
# - Estiver entre aspas duplas triplas  -> """uma string""", """123""", """a""", """true""", """42.3"""
"""
nome = 'Geek Unversity'
print(nome)
print(type(nome))

nome = "Gina's Bar"  # Caso seja preciso incluir uma palavra que utilize aspas simples, é recomendado usar aspas duplas,
# na definição da string
print(nome)
print(type(nome))

nome = "Dhionathan Jobim"
print(nome)
print(type(nome))
"""
# Convertendo string pra maiúscula uppercase
nome = 'Dhionathan Jobim'
print(nome.upper())

# Convertendo string pra minúsculo lowercase
nome = 'Dhionathan Jobim'
print(nome.lower())

# Convertendo string para uma lista
nome = 'Dhionathan Jobim'
print(nome.split())

# Funcionamento de uma string
# [0,    1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14, 15,
# ['D', 'h', 'i', 'o', 'n', 'a', 't', 'h', 'a', 'n', ' ', 'J', 'o', 'b', 'i', 'm']
nome = 'Dhionathan Jobim'
print(nome[0:14])  # Slice de String
print(nome.upper()[4:16]) # Slice de string

# Lista funcionamento
# [      0,        1]
# ['Dhionathan' 'Jobim']
print(nome.split()[0])
print(nome.split()[1])
print(nome.split()[0:2])

nome = 'Dhionathan Jobim'
"""
[::-1] -> Comece do primerio elemento, vá até o último elemento e inverta
"""
print(nome[::-1])  # Metódo Pythônico de inversão para string.

print(nome.replace('n', 'p'))  # Troque todas as letras 'n' da string por 'p'.

texto = 'socorram me subino onibus em marrocos'  # Exemplo de palíndromo no qual a frase permanece igual
# mesmo se escrita ou lida de trás pra frente
print(texto)
print(texto[::-1])


