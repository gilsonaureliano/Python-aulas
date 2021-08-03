from random import randint
from time import sleep
sorte = []
p = []
print('+='*20)
print('{:^40}'.format('LOTERIA BOA SORTE'))
print('+='*20)
a = int(input('Quantas apostas deseja: '))
print('+='*3, f'SORTEANDO {a} JOGOS', '+='*3)
for t in range(0, a):
    for c in range(0, 6):
        s = int(randint(1, 60))
        while True:
            if s not in p:
                p.append(s)
                break
            else:
                s = int(randint(1, 60))
    p.sort()
    sorte.append(p[:])
    p.clear()
    print(f'Seu jogo Nº {t + 1} é {sorte[t]}')
    sleep(3)