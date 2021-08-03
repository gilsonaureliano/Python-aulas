pessoas = {'nome':'Gilson', 'Idade':55, 'Sexo': 'M'}
print(pessoas)
print(pessoas['nome'])
print(pessoas['Idade'])
print(f'{pessoas["nome"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.values():
    print(k)
for k ,v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'UF':'Rio de Janeiro', 'SIGLA' : 'RJ'}
estado2 = {'UF':'PERNAMBUCO', 'SIGLA':'PE'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(estado2)

estado3 = dict()
brasil1 = list()
for c in range(0, 3):
    estado3['UF'] = str(input('Estado: '))
    estado3['SIGLA'] = str(input('SIGLA: '))
    brasil1.append(estado3.copy())
print(brasil1)