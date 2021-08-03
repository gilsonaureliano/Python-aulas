s = n = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print('Soma {}'.format(s))
print(f'A soma - outro print {s}')
print(f'Com centralização {s:-^20}')
