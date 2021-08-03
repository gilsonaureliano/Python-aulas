n = 0
c = 0
d = 0
t = 0
while not n == 999:
    c = c + 1
    t = t + d
    d = int(input('Digite um numero [999 para parar]: '))
    n = d
print('{} numeros digitador, total {}'. format(c - 1 , t))