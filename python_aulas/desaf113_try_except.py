def leiaint(a):
    while True:
        try:
            a = str(input('Digite um numero Inteiro: '))
            a = int(a)
        except ValueError:
            print('\33[31mERRO, digite um numero inteiro válido!\33[m')

        except KeyboardInterrupt:
            print('\33[35mO usuario não desejou digitar!\33[m')
            return 0

        else:
            return a


def leiafloat(b):
    while True:
        try:
            b = str(input('Digite um numero REAL: '))
            b = float(b)
        except ValueError:
            print('\33[34mERRO, digite um numero REAL válido!\33[m')
            continue
        except KeyboardInterrupt: # não funciona
            print('\33[35mO usuario não desejou digitar!\33[m')
            return 0




        else:
            return b


# programa principal
n = leiaint('')
f = leiafloat('')
print(f'Você digitou o numero inteiro {n} e o real {f}')
