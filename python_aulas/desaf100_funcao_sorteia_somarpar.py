from random import randint
from time import sleep


def sorteio():
    print(f'Sorteando o 5 valos da lista: ', end=' ')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(numeros[c], end=' ')
        sleep(0.4)
    print('PRONTO!')


def somapar(num):
    par = 0
    for d in num:
        if d % 2 == 0:
            par += d
    print(f'Somando os valosres de {numeros} temos o total de {par} ')


numeros = []
sorteio()
somapar(numeros)
