print('=' * 35)
print('{:^30}'.format('BANCO CEV'))
print('=' * 35)
while True:
    valor = (input('Qual o valor você quer sacar: '))
    r = valor.isnumeric()
    if r:    #já está sub entendido se for VERDADE (True)
        valor = int(valor)
        break
    else:
        print('Opção invalida, tente novamente! ')
        print('+' * 35)
c = 0
while True:
    if (valor / 50) >= 1:
        c += 1
        valor = valor - 50
    else:
        break
if c > 0:
    print(f'Total de {c} cédulas de R$ 50,00')
c = 0
while True:
    if valor / 20 >= 1:
        c += 1
        valor = valor - 20
    else:
        break
if c > 0:
    print(f'Total de {c} cédulas de R$ 20,00')
c = 0
while True:
    if valor / 10 >= 1:
        c += 1
        valor = valor - 10
    else:
        break
if c > 0:
    print(f'Total de {c} cédulas de R$ 10,00')
c = 0
while True:
    if valor / 1 >= 1:
        c += 1
        valor = valor - 1
    else:
        break
if c > 0:
    print(f'Total de {c} cédulas de R$ 1,00')
print('=' * 35)
print('Volte sempre ao Banco CEV! Tenha um bom dia!')
