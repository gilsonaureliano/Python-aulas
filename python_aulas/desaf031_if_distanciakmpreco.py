viagem = int(input('Qual a distancia da sua viagem em Km: '))
print("""Preço da km = R$ 0,50 até 200 km,
e  acima de 200 km, o km custa = R$ 0,45""")

print('='*15,'Calculo','='*15)

if viagem <= 200:
    print('Você vai pagar - <= 200 km: R$ {}'.format(viagem * 0.5))
else:
    print('Você vai pagar - > 200: R$ {}'.format(viagem * 0.45))
print('='*40)