cont = c3 = 0
a = (int(input('Digite um numero: ')), int(input('Digite mais um numero: '))
     ,int(input('Digite outro numero: ')),int(input('Digite o ultimo numero: ') ))
print(f'Você digitou os valor: {a}')
for c in range (0 ,4):
    if a[c] == 9:
        cont += 1
print(f'Apareceu {cont} vezes o numero 9.')
print(f' O NUMERO 9 APARECEU {a.count(9)} VEZES.')

while True:
    for ct in a:
        if ct == 3:
            p = a.index(3) + 1
            print(f'O valor 3 foi digitado na posição {p}')
        else:
            c3 += 1
            if c3 > 3:
                print('O valor 3 não foi digitado')
    break
while True:
    print('Os numeros pares digitados foram: ', end=' ')
    for ct in a:
        if ct % 2 == 0:
            print(ct ,end=' ')
    break
