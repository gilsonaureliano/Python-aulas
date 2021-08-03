from random import randint
from operator import itemgetter
jogo = {'Jogador': 0, 'dado': 0}
lista = []

for c in range(0, 5):
    jogo['Jogador'] = c + 1
    jogo['dado'] = randint(1, 6)
    lista.append(jogo.copy())
    print(f' O jogador {lista[c]["Jogador"]} sorteou o numero {lista[c]["dado"]}')
print('++'*15)
print(f'{"RANKING":^30}')
print('++'*15)
ordenar = sorted(lista, key=itemgetter("dado"))
ordenar.reverse()
for k ,v in enumerate(ordenar):
    print(f'{k + 1}ºlugar - Jogador {v["Jogador"]} = Sorteou  {v["dado"]}')