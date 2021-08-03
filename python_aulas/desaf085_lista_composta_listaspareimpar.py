lt = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
         lt[0].append(n)
    else:
        lt[1].append(n)
lt[0].sort()
lt[1].sort()
print(f'Os valores pares digitados foram {lt[0]}')
print(f'Os valores impares foram {lt[1]}')
