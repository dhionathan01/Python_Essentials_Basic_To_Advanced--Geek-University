# Essa comprhesion só retorna os nomes que começam com a inicial C.
nomes = ['Carlos', 'Camila', 'Carla', 'Cassino', 'Cristina', 'Daniel', 'Junior', 'Marcos']
print([nome for nome in nomes if nome[0] == 'C'])
# Valida quais contem nome com inicial C.
print([nome[0] == 'C' for nome in nomes])
