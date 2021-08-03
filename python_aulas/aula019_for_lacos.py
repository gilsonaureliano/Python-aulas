for c in range (0,6):
    print('Ola')
print('FIM')

for c in range (0,6):
    print(c)
print('FIM')

for c in range (6,0,-1):
    print(c)
print('FIM')

n = int(input('Digite um numero: '))
for c in range(0, n):
    print(c)
print("Acabou")

s = 0 # somatorio
for c in range(0,4):
    a = int(input('Digite o {}º valor: '.format(c +1)))
    s += a       #s = s + a (essa é a torma tradicional de somar

print('A SOMA É {}'.format(s))
