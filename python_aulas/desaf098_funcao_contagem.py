from time import sleep


def contagem(lst):
    print('-=' * 17)
    print(' Contagem 1 ate 10 de 1 em 1')
    for c in range(1, 11):
        print(f'{c} ', end=' ')
        sleep(0.5)
    print('FIM')
    print('-=' * 17)
    print(' Contagem 10 ate 0 de 2 em 2')
    for c in range(10, 0, -2):
        print(f'{c} ', end=' ')
        sleep(0.5)
    print('FIM')
    print('Agora é sua vez de persolizar a contagem')
    lst[0] = int(input('Inicio: '))
    lst[1] = int(input('FIM: '))
    lst[2] = int(input('Passo: '))
    print('-=' * 17)
    if lst[2] == 0:
        lst[2] = 1
    if lst[0] > lst[1] and lst[2] > 0:
        lst[2] = lista[2] * (-1)
    print(((f' Contagem de {lst[0]} até {lst[1]} de'
            f' {lst[2] if lst[2] > 0 else lst[2] * (-1)} em {lst[2] if lst[2]>0 else lst[2] * (-1) } ')))
    for c in range(lst[0], lst[1], lst[2]):
        print(c, end=' ')
        sleep(0.1)
        if c == lst[1] - lst[2]:
            print(lst[1], end=' ')
    print('FIM')


lista = [0, 0, 0]
contagem(lista)

