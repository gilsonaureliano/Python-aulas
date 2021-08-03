matriz = []
m = []
tt = tc = tl = mv = 0
for c in range(0, 3):
    for t in range (0, 3):
        m.append(int(input(f'Digite um valor para ({c},{t})= ')))
        matriz.append(m[:])
        m.clear()
print('+='*20)
for c in range(0, 3):
    print(f'{matriz[c]}', end=' ')
print()
for c in range(3, 6):
    print(f'{matriz[c]}', end=' ')
print()
for c in range (6, 9):
    print(f'{matriz[c]}', end=' ')
print()
print('+='*20)
for c in range(0, 9):
    if matriz[c][0] % 2 == 0:
        tt += matriz[c][0]
print(f'A soma total dos valores pares  é {tt}')
for c in range(2, 11, 3):
    tc += matriz[c][0]
print(f'A soma da terceira coluna é {tc}')
for c in range(3, 6):
    if c == 3:
        mv = matriz[c][0]
    else:
        if matriz[c][0] > mv:
            mv = matriz[c][0]
print(f'O maior valor da segunda linha é {mv} ')
