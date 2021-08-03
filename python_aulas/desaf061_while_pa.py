n = int(input('Qual o primeiro valor da PA: '))
r = int(input('Qual a razão da PA: '))
p = n - r
while p < (n + (9 * r)):
    p = p + r
    print('{}'.format(p), end= ' ')
