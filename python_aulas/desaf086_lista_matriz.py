matriz = []
m = []
for c in range(0, 3):
    for t in range (0, 3):
        m.append(int(input(f'Digite um valor para ({c},{t})= ')))
        matriz.append(m[:])
        m.clear()
for c in range(0, 3):
    print(f'{matriz[c]}', end=' ')
print()
for c in range(3, 6):
    print(f'{matriz[c]}', end=' ')
print()
for c in range (6, 9):
    print(f'{matriz[c]}', end=' ')
