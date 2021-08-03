from datetime import date
atual = date.today().year
m = 0
mn = 0
for c in range (0 , 7 ):
    ano = int(input('Qual o ano do seu nascimento: '))
    if atual - ano > 21:
        m = m + 1
    else:
        mn = mn + 1
print('Foram {} maiores e {} menores de idade'.format(m,mn))

