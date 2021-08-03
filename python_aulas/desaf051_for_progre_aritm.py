n = int(input('Qual o primeiro valor da P.A.: '))
r = int(input('Qual a Razão da PA (r = a2 -a1): '))
pa = 0
for c in range(n, n + (r * 10), r):  # vai mostrar os 10 numeros de uma PA
    pa = pa + c
    print('{} '.format(c), end='-> ')
print('A soma é {}'.format(pa))
