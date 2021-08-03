num = list()
par = list()
imp = list()
while True:
    num.append(int(input('Digite um valor: ')))
    s = str(input('Quer continuar [S/N]: ')).upper()[0].strip()
    if s in 'N':
        break
print(f'Os valores digitados foram: {num}')
for c in range(0, len(num)):
    if num[c] % 2 == 0:
        par.append(num[c])
    else:
        imp.append(num[c])
print(f'A lista par é {par}')
print(f'A lista impar é {imp}')
