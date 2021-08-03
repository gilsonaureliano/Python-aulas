sexo = str(input('Informe seu sexo: ')).upper()
if sexo in "FM":
    print('Sexo registrado, obrigado! ')
else:
    while sexo not in 'FM':
        rs = str(input('Resposta errada, digite noevamente: ')).upper()
        sexo = rs
    print('Registrado com sucesso')
