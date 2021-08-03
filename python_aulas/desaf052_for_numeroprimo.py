n = int(input('Digite um numero inteiro: '))
p = 0
for c in range(1 , n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        p = p +1
    else:
        print('\033[35m', end=' ')
    print('{}'.format(c), end=' ')
if p == 2:
    print('\n\033[33m {} é um numero primo'.format(n))
else:
    print('\n\033[35m {} NÃO É NUMERO PRIMO'.format(n))
