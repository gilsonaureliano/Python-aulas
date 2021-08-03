casa = float(input('Qual o valor da casa R$: '))
sal = float(input('Qual o valor de seu salario R$: '))
ano = int(input('Em quantos anos você deseja pagar: '))
pmensal = casa / (ano * 12)
if pmensal >= (sal * 30 / 100):
    print('\033[031m Emprestimo negado - passou o limite maximo de 30% do salario \033[m', end='')
    print('Obrigado ')
else:
    print('\033[033m Emprestimo aprovado')
    print(" Sua parcela será de R$ {}{:.2f}{} ".format('\033[031m',  pmensal, '\033[m'))
print('obrigado')
