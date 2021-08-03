# Ler um numero no teclado e mostra a parte inteira ex 6.9859 retorna 6
from math import floor, trunc
# tres formas de resolver
n1 = float(input('Digite um numero: '))
print(floor(n1))

print('O numero digitado foi {} e a parte inteira é {}'.format(n1, trunc(n1)))

print('Outra forma de mostrar a porção inteira -> {}'.format(int(n1)))
