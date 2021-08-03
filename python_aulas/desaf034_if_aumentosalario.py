sal = float(input('Digite o valor do salario em R$: '))
if sal > 1250:
    print('Seu novo salario com 10% é de: R$ {}{:.2f}'.format('\033[33m', sal+(sal*10/100)))
else:
    print('Seu novo salario com 15% é de R$ {}{:.2f}{}'.format('\033[7;34m', sal +(sal*15/100), '\033[m'))
n = 'prova de python'
print(len(n))