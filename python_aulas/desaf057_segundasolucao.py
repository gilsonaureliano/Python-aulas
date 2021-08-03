sexo = str(input('Sexo: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Errado, digite novamente: ')).upper()[0]
print('Registrado')
