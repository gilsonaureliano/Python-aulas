p = list()
c = 0
while True:
    p.append(int(input('Digite um numero: ')))
    c += 1
    s = str(input('Quer continuar [S/N]')).upper()[0]
    if s in 'N':
        break
print(f'Foram digitados {c} valores')
p.sort(reverse=True)
print(f'O valores em ordem descrecente {p}')
if 5 in p:
    print('Sim, 5 faz parte da lista')
else:
    print('5 Não faz parte')
