n1 = float(input('Qual a sua nota: '))
n2 = float(input('Qual a segunda nota: '))
m = (n1+n2)/2
print('Sua media foi {:.1f}'.format(m))
if m >= 6:

    print('Aprovado, PARABÉNS!')
else:
    print('ESTUDE MAIS')
