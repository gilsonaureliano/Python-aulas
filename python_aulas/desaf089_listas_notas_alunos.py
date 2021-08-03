geral = []
nome = []
nota = []
while True:
    nome.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    m = (nota[0] + nota[1]) / 2
    nome.append(nota[:])
    nome.append(m)
    nota.clear()
    geral.append(nome[:])
    nome.clear()
    s = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if s in 'N':
        break
print('+='*30)
print('{} {:^10} {:^11}'.format('No', 'NOME', 'MÉDIA'))
for c in range(0, len(geral)):
    print('{:<3} {:<14} {:.1f}'.format(c, geral[c][0], geral[c][2]))
while True:
    al = int(input('Mostrar notas de qual aluno? {999 para sair]: '))
    if al == 999:
        break
    if al <= len(geral) - 1:
        print(f'Notas de {geral[al][0]} são {geral[al][1]}')
print('FIM')
print(f'{"MADIA":^20}{"BOM":^30}   ')