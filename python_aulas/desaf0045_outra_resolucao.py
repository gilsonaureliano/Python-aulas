from random import randint

itens = ('Pedra', 'Papel', 'Tesoura', '****') # aqui foi montada uma lista
computador = randint(0, 2)

print("""Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura """)
jogador = int(input('Qual e sua opção de jogada: '))
if jogador <= 2:
    teste = jogador
else:
    teste = 3

print('-='*11)
print('Computador {}'.format(itens[computador])) # a varialvel computador sorteia um numero entre 0,1,2 (posição lista
print('Jogador {} '.format(itens[teste]))
print('-='*11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGOU ERRADO')
elif computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('JOGADOU GANHOU')
    else:
        print('JOGOU ERRADO')
elif computador == 2:
    if jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGOU ERRADO')