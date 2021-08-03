print('{:=^40}'.format(' MILENA MOVEIS '))
preco = float(input('Qual o preço do produto R$: '))
print(' ')
print('Escolha uma das opções abaixo para pagamento')
print('-=' * 25)
print('\033[35m[1] À vista: dinheiro ou cheque - 10% desconto')
print('[2] À vista no cartão - 5% desconto')
print('[3] 2 x cartão - preço normal')
print('[4] 3 x ou mais no cartão - 20% de juros\033[m')
print('-=' * 25)
pag = int(input('Qual a sua escolha de pagamento: '))

if pag == 1:
    dc = preco * 10 / 100
    nv = preco - dc
elif pag == 2:
    dc = preco * 5 / 100
    nv = preco - dc
    print('==' * 25)
    print('Serão 2 parcelas de R$ {:.2f}'.format(nv / 2))
elif pag == 3:
    nv = preco
elif pag == 4:
    p = int(input('Em quantas parcela: '))
    dc = preco * 20 / 100
    nv = preco + dc
    pg = nv / p
    print('==' * 25)
    print(' ')
    print('Você vai pagar {} parcelas de R$ {:.2f} com JUROS'.format(p, pg))
else:
    nv = 0
    print('Voce digitou errado')
print(' ')
print('==' * 25)
print('Seu novo preço é {}R$ {:.2f}{}'.format('\033[32m', nv, '\033[m'))
print('==' * 25)
