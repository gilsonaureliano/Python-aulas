km = int(input('Qual a velocidade do seu carro KM/h? '))
if km > 80:
    print('Voce foi multado pois ultrapassou a velocidade maxima. sua velocida é {} km/h'.format(km))
    print('Você vai pagar de multa: R$ {:.2f}'.format((km-80)*7))
else:
    print('Boa Viagem')
