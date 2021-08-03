n1 = int(input('Digite um numero '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 > n2 > n3:
    print('{} é o maior numero1'.format(n1))
    print('{} é o menor numero'.format(n3))
if n1 < n2 < n3:
    print('{} é o maior numero2'.format(n3))
    print('{} é o menor numero'.format(n1))
if n1 < n2 > n3 > n1:
    print('{} é o maior numero3'.format(n2))
    print('{} é o menor numero'.format(n1))
if n1 < n2 > n3 < n1:
    print('{} é o maior numero4'.format(n2))
    print('{} é o menor numero'.format(n3))
if n1 > n2 < n3 > n1:
    print('{} é o maior numero5'.format(n3))
    print('{} é o menor numero'.format(n2))
if n1 > n2 < n3 < n1:
    print('{} é o maior numero6'.format(n1))
    print('{} é o menor numero'.format(n2))
print('='*100)
print('')
# Para escolher o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# para escolher o maior
maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Valor maior {}'. format(maior))
print('Valor MENOR {}'. format(menor))
