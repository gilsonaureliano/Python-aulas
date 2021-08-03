import math

n1 = (input('Digite um numero entre "0" e "9999": '))
n2 = n1.zfill(4)
print(n2 , type(n2))
print('Unidade: {:2} '.format(n2[3]))
print('Dezena:  {:2} '.format(n2[2]))
print('Centena: {:2} '.format(n2[1]))
print('Milhar:  {:2} '.format(n2[0]))

n3 = int(n2)    # resulução da questão usando a matemática
print(n3 , type(n3))

n = n3 // 1 % 10
d = n3 // 10 % 10
c = n3 // 100 % 10
m = n3 // 1000 % 10

print('Unidade: {}'. format(n))
print('Dezena:  {}'. format(d))
print('Centena: {}'. format(c))
print('Milhar:  {}'. format(m))