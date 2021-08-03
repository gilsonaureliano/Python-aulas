cidade = str(input("Escreva o nome de uma cidade: ")).strip()  # verifica se o nome da cidade começa com santo.
cidade = cidade.lower()
print(cidade[:5] == 'santo')
cidade = cidade.split()

sim = 'santo' in cidade[0]
print('A cidade começa com a palavra SANTO? : ', sim)


