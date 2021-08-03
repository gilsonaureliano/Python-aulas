l1 = []
l2 = []
l3 = []
tp = 0
maip = mep = 0
while True:
    l2.append(str(input('Nome: ')))
    l2.append(int(input('Peso [Kg]: ')))
    l1.append(l2[:])
    l2.clear()
    tp += 1
    s = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if s in 'N':
        break
print(f'Foram cadastradas {tp} pessoas')
for c in l1:
    if c[1] >= maip:
        maip = c[1]
print(f'O maior peso foi de {maip} kg.', end=' ')
for c in l1:
    if c[1] == maip:
        l3.append(c[0])
        print(l3, end=' ')
        l3.clear()
for c in range(0, len(l1)):
    if c == 0:
        mep = l1[c][1]
    elif l1[c][1] < mep:
        mep = l1[c][1]
print(f'\nO menor peso foide {mep}.', end=' ')
for c in range(0, len(l1)):
    if l1[c][1] == mep:
        l3.append(l1[c][0])
        print(l3, end=' ')
        l3.clear()
print('\nFIM')
