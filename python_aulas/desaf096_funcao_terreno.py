def area(l, c):
    s = l * c
    print(f'O terreno {a} x {c} tem uma area de {s:.2f}m²')


# programa principal
print('Controle de terreno')
print('-'*15)
a = float(input('Lagura (m): '))
c = float(input('Comprimento (m): '))
area(a, c)
