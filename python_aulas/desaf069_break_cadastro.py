msexo = 0
maior18 = fsexo = 0
while True:
    print('+' * 20)
    print("Cadastro de Pessoas")
    print('+' * 20)
    while True:
        idade = (input('Idade = '))
        v = idade.isnumeric()
        if v:
            idade = int(idade)
            break
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if sexo in 'FM':
            break
    while True:
        p = str(input('Quer Continuar [S/N]: ')).upper().strip()[0]
        if p in 'SN':
            break
    if idade > 18:
        maior18 += 1
    if sexo in "M":
        msexo += 1
    if sexo in 'F' and idade < 20:
        fsexo += 1
    if p in 'N':
        break
print('+=' * 20)
print(f"""Foram cadastrados {maior18} pessoas maior 18 anos
Homens são: {msexo}
Mulherees menor 20 anos foram: {fsexo}""")
print('+=' * 20)
print('FIM CADASTRO')
