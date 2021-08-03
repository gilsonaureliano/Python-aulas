from random import randint
cp = randint(0,10)
print(cp)
j = int(input('Digite seu numero de 0 a 10): '))
c = 1
while j != cp:
    if cp > j:
        print('Tente um numero maior')
    else:
        print('Tente um numero menor')
    j = int(input('Digite novamente: '))
    c += 1
print('o PC jogou {} e você na {}° tentativa, acertou'.format(cp, c))
print('FIM DE JOGO')
