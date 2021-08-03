from random import randint
from time import sleep
print('Aqui é seu computador, vou pensar em um numero de 0 a 5. Você consegue descobrir?')
print('+'*40)
n2 = int(input('Digite um numero de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
n1 = randint(0,5)
if n1 == n2:

    print('Parabens você venceu, processei {} e você digitou {}'. format(n1, n2))
else:
    print('Voce perdeu! eu processei {} e você digitou {}'.format(n1, n2))
