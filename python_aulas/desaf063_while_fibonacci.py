n = int(input('Fibonacci numero: '))
i = 0
n3 = 1
n1 = -1
n2 = 1
while i < n:
    i = i + 1
    n3 = n2 + n1
    n1 = n2
    n2 = n3
    print('{}'. format(n3), end="-> ")
print('FIM')
