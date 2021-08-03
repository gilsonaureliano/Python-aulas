from time import sleep


def maior(*lst):
    mv = 0
    print('-=' * 20)
    print('Analisando os dados passados')
    for c in range(0, len(lst)):
        print(lst[c], end=' ')
        sleep(0.5)
        if lst[c] > mv:
            mv = lst[c]
    print(f'Foram informados {len(lst)} valores ao todo.')
    print(f'O maior valor informado foi {mv}.')


maior(9, 6, 5, 8, 0)
maior(4, 7, 2)
maior(1, 2)
maior(6)
maior()
