from random import randint
maiorvalor = menorvalor = 0
tupla = (randint(0 , 10), randint(0 , 10) , randint(0 , 10) , randint(0 , 10) , randint(0 , 10))
print(f' Os numeros sorteados foram: {tupla}')
for c in range (0 , 5):
    for a in range (0,5):
        if c == a == 0:
            maiorvalor = tupla[0]
            menorvalor = tupla[0]
        elif tupla[a] > maiorvalor:
            maiorvalor = tupla[a]
        if tupla[a] < menorvalor:
            menorvalor = tupla[a]
print(f'Maior valor {maiorvalor}')
print(f'Menor valor {menorvalor}')
print(f'MAIOR VALOR {max(tupla)}')
print(f'MENOR VALOR {min(tupla)}')
