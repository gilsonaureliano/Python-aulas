n = int(input('Qual o primeiro valor da PA: '))
r = int(input('Qual a razão da PA: '))
p = n - r
m = 10
while p < (n + (9 * r)):
    p = p + r
    print('{}'.format(p), end=' ')

r1 = int(input('Digite zero se deseja sair ou quantidade da PA: '))
p1 = p
m = m + r1
while not r1 == 0:
    while p1 < (p + (r1 * r)):
        p1 = p1 + r
        print('{}'.format(p1), end=' ')
    r1 = int(input('Deseja continuar: '))
    p = p1
    m = m + r1
print('{} termos foram mostrados'. format(m))
print('FIM')
