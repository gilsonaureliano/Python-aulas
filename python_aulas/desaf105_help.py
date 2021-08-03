def hel(msg):
    while True:
        t = len(msg)
        print('\33[30;42m~' * (t + 4))
        print(f'{msg}')
        print('~' * (t + 4))
        n = str(input('\33[mFunção ou Biblioteca >> '))
        if n not in 'fim':
            print('\33[30;44m~' * (30 + len(n)))
            print(f' ACESSANDO O MANUAL DECOMANDO {n}')
            print(f'~' * (30 + len(n)))
            print(f'\33[m', end='')
            print(f'\33[7;40m ', end='')
            print(f'{help(n)}')
            print(f'\33[m', end='')
        else:
            print('\33[30;41m~' * 10)
            print( ' ATÈ LOGO ' )
            print('~' * 10)
            break


#programa principal
hel(' Sistema de Ajuda PyHelp ')
