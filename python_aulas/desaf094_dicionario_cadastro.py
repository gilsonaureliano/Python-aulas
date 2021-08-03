pes = dict()
lit = list()
t = {}
tp = tidade = 0
while True:
    pes['nome'] = str(input('Nome: '))
    while True:
        pes['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pes['sexo'] in 'MF':
            break
        print('ERRO')
    pes['idade'] = int(input('Idade: '))
    tidade += pes['idade']
    lit.append(pes.copy())
    tp += 1
    s = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if s in 'N':
       break
print('-='*30)
print(f'Foram cadastradas {tp} pessoas')
print(f'A média da idade é {tidade/len(lit):.1f}')
print(f'As mulheres cadastradas foram: ', end=' ')
for c in range(0, len(lit)):
    if lit[c]['sexo'] in 'F':
        print(f'{lit[c]["nome"]}', end= ' ')
print('\nLista das pessoas que estão acima da média')
print(' ')
for c in range(0, len(lit)):
    t = lit[c]
    if lit[c]['idade'] > (tidade/len(lit)):
        for k, v in t.items():
            print(f'{k} = {v};', end=' ')
        print('\n')
print('FIM')
