ma = 0
me = 0
for c in range(1,6):
    peso = float(input('Qual o seu peso (kg): '))
    if c == 1:
        ma = peso
        me = peso
    else:
        if peso > ma:
            ma = peso
        if peso < me:
            me = peso
print('O maior peso foi {}kg \nO menor peso foi {}kg'.format(ma , me))
