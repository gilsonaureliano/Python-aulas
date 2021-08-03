a = float(input('Digite o valor da 1° reta: '))
b = float(input('Digite o 2º valor: '))
c = float(input('Digite o 3° valor: '))

#    | b - c | < a < b + c
#    | a - c | < b < a + c
#    | a - b | < c < a + b

if b - c < a < b + c:
    if a - c < b < a + c:
           if a - b < c < a + b:
                  print(' As retas {} , {} e {} formam um TRIANGULO'. format(a, b, c))
           else:
               print('As retas não formam um TRIANGULO')
    else:
        print('As retas não formam um TRIANGULO')
else:
     print('As retas não formam um TRIANGULO')

# FORMA MAIS SIMPLES

print('-='*100)

if a < b + c and b < c + a and c < b + a:
    print(" AS RETAS FOMAM UM TRIANGULO")
else:
    print('NAO È UM TRIANGULO')