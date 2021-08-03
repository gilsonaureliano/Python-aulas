n = int(input('Numero para fatorial: '))
f = 0
tft = 1
while f < n:
    print('{}'.format(n-f), end=' ')
    print('x' if f < n -1 else '=', end=' ')
    n1 = n - f
    f = f + 1
    tft = tft * n1
print('Resultado: {}'.format(tft))
d1 = 0
ft = 1
d = int(input('Fatorar: '))
for c in range (0, d):
    ##print('{}'.format(c), end=' ')
    d1 = d - c
    print('{}'.format(d1), end=' ')
    ft = ft * d1
print('Resultado: ', ft)