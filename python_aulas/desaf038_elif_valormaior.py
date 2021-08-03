n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O \033[32m primeiro valor {} é maior \033[m que o segundo {}'.format(n1, n2))
elif n2 > n1:
    print(f'O \033[35m segundo valor {n2} é maior \033[m que o primeiro {n1}')
elif n1 == n2:
    print('\033[33m Os valores são iguais \033[m {} = {}'.format(n1, n2))
