def leiaint(a):
    while True:
        a = str(input('Digite um numero: '))
        if a.isnumeric():
            return a
        else:
            print('\33[31mERRO, digite um numero inteiro válido!\33[m')


#programa principal
n = leiaint('Digite um numero: ')
print(f'Você digitou o numero {n}')