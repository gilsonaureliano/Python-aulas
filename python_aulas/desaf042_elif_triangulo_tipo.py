a = float(input('Primeiro valor da reta: '))
b = float(input('Segundo valor da reta: '))
c = float(input('Terceiro valor da reta: '))
if a < (b + c) and b < (c + a) and c < (a + b):
    print('As retas {} , {} , {} formam um triangulo'.format(a, b, c))
    if a == b == c:
        print('As retas formam um \033[33m triangulo EQUILATERO')

    if a != b and b != c and a != c:
        print('As retas formam um \033[31m triangulo ESCALENO')

    if a != b == c or b != a == c or c != a == b:
        print('As retas formam um \033[32m triangulo ISOSCELES')

    h = a  # para ver se é triangulo retangulo
    co = b
    ca = c
    # print(h, co, ca)
    if a < b > c:
        h = b
        co = a
        ca = c
    if a < c > b:
        h = c
        co = a
        ca = b
    if h ** 2 == co ** 2 + ca ** 2:
        print('As retas formam um triangulo RETANGULO')
    print('\033[mFIM')

else:
    print('\033[41mAs retas NÃO FORMAM TRIANGULO')
