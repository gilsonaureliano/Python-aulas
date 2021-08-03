from datetime import date
data = int(input("Qual o ano do seu nascimento: "))
hj = date.today().year
ide = hj - data
print('\033[31m''-='*20)
print('{:>21} {} anos'.format('Sua idade é', ide))
if ide <= 9:
    print('{:^40}'.format('Categoria MIRIM'))
elif 9 < ide <= 14:
    print('{:^40}'.format('Categoria INFANTIL'))
elif 14 < ide <= 19:
    print('{:^40}'.format('Categoria JUNIOR'))
elif 19 < ide <= 20:
    print('{:^40}'.format('Categoria SENIOR'))
elif ide > 20:
    print('{:^40}'.format('Categoria MASTER') )
print('\033[31m''-='*20)
