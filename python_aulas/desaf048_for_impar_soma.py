s = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        print(c)
        s = s + c
print('A soma é {}'.format(s))
