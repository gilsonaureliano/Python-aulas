s = 0
t = 0
for c in range(1, 7):
    n = int(input('Digite {}º valor: '.format(c)))
    if n % 2 == 0:
        t = t + 1
        s = s + n
print('Você digitou {} numeros pares e a soma dos pares é {}'.format(t, s))
