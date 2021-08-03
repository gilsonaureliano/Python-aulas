n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))


sair = False
while not sair:
    print('+' * 15, 'OPÇÕES', '+' * 15)
    print("""    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] TROCAR NUMEROS
    [5] SAIR """)
    print('+'*50)
    s = int(input('Qual a sua opção: '))
    if s == 1:
        r = n1 + n2
        print('SOMA = {} '.format(r))
    elif s == 2:
        r = n1 * n2
        print('A multiplicação de {} * {} = {}'.format(n1 , n2, r))
    elif s == 3:
        r = n1
        if n1 < n2:
               r =n2
        else:
            if n1 == n2:
                r = '++++IGUAIS+++++'
        print('Entre {} e {} o maior é {}'. format(n1, n2, r))
    elif s == 4:
        n1 = float(input('\033[33mDigite o primeiro NOVO valor: '))
        n2 = float(input('\033[35mDigite o segundo NOVO valor:\33[m'))
    elif s == 5:
        sair = True
        print('SAINDO DO CALCULO')
    else:
        print('Você digitou invalido, tente novamente')
