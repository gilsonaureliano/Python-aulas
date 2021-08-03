n1 = int(input('Qual o numero será convertido: '))
print('-=' * 40)
print('Digite sua escolha')
print('[1] Binario')
print('[2] Octal')
print('[3] Hexadecimal')
print('-=' * 40)
d = str(input('Qual a sua escolha?: '))
print('========CONVERSÃO==========')

if d == '1':
    c = str(bin(n1)[2:])    # [2:] fatiando o str para aparecer apenas depois de 2 casas
    print('Em binario é {}'.format(c))
elif d == '2':
    c = str(oct(n1)[2:])
    print('Em octal é {}'.format(c))
elif d == '3':
    c = str(hex(n1)[2:])
    print('Em Hexadecimal é {}'.format(c))

else:
    print('Escolha errada')
