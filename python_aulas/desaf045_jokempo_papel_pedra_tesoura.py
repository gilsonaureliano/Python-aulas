import time
from random import randint
from emoji import emojize
from time import sleep


e1 = (emojize(' :raised_hand:', use_aliases=True))
e2 = (emojize(' :v:', use_aliases=True))
e3 = (emojize(' :facepunch:', use_aliases=True))
print('=' * 40)
print('\033[35m[1] PAPEL  {}'.format(e1))
print('[2] TESOURA {}'.format(e2))
print('[3] PEDRA  {}\033[m'.format(e3))
print('=' * 40)

n1 = randint(1, 3)
# print(n1)

n2 = int(input('Escolha um numero entre 1 a 3: '))
if n2 == 0 or n2 > 3:
    print('OPÇÃO INVALIDA')
else:
    print('='*40)
    print('PROCESSANDO ...')
    sleep(3)
    if n1 == n2:
        if n1 == 1:
            j1 = e1
            j2 = e1
        if n1 == 2:
            j1 = e2
            j2 = e2
        if n1 == 3:
            j1 = e3
            j2 = e3

        print('\033[7;33m     EMPATE     \033[m')

    else:
        if n1 == 2 and n2 == 1 or n1 == 1 and n2 == 3 or n1 == 3 and n2 == 2:
            print('\033[7;31m     VOCÊ PERDEU     \033[m ')
        else:
            print('\033[7;32m     VOCÊ VENCEU     \033[m')
    # print(' PC' , n1)
    # print('VOCÊ' , n2)

    if n1 == 2 and n2 == 1:
        j1 = e2
        j2 = e1
    if n1 == 1 and n2 == 3:
        j1 = e1
        j2 = e3
    if n1 == 3 and n2 == 2:
        j1 = e3
        j2 = e2
    # +++++++++++++++++++++++++++++++
    if n2 == 2 and n1 == 1:
        j2 = e2
        j1 = e1
    if n2 == 1 and n1 == 3:
        j2 = e1
        j1 = e3
    if n2 == 3 and n1 == 2:
        j2 = e3
        j1 = e2

    print('Você {} x{} Computador'.format(j2, j1))
