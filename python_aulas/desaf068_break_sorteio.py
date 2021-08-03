from random import randint
c = 0
while True:
    computador = randint(0, 10)
    print('+='*12)
    print('Vamos jogar par ou ímpar?')
    print('+='*12)
    jogador = int(input('Digite seu valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Impar? ')).upper().strip()[0]
    if (computador + jogador) % 2 == 0:
        r = 'DEU PAR'
        p2 = 'P'
    else:
        r = 'DEU IMPAR'
        p2 = 'I'
    print(f'O computador jogou {computador} e você jogou {jogador} ,total {computador + jogador} - {r}')
    if pi == p2:
        print('+='*12)
        print('Você Venceu!!')
        print('Vamos jogar novamente')
        c = c + 1
    else:
        print('+=' * 12)
        print('Você PERDEU!!')
        print(f'GAME OVER - você venceu {c} vezes')
        break
