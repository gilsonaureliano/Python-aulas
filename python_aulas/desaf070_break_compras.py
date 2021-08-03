menornome = ' '
tcompras = maior = c = menor = 0
print('='*25)
print('    LOJA BARATA    ')
print('='*25)
while True:
    nome = str(input('Qual o nome do produto: '))
    while True:
        preco = (input('Preço R$: '))
        v1 = preco.replace('.', '')
        v = v1.isdigit()
        if  v:
            preco = float(preco)
            break
    print('-'*20)
    tcompras += preco
    if preco > 1000:
        maior += 1
    c += 1
    if c == 1:
        menor = preco
        menornome = nome
    if preco < menor:
        menor = preco
        menornome = nome
    while True:
        p = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
        if p in 'SN':
            break
    print('-'*20)
    if p in 'N':
        break
print(f'Total das compras R$ {tcompras}')
print(f' Foram {maior} compras maior de 1.000 Reias')
print(f'O prioduto: {menornome} foi o menor preço {menor}')


print('FIM DAS COMPRAS')
