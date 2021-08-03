pat = {}
gol = []
tg = 0
final = []
while True:
    pat['nome'] = str(input('Nome do Jogador: '))
    p = int(input('Quantas partidas jogou: '))
    for c in range(0, p):
        g = int(input(f"Quantos gols na partida {c}: "))
        gol.append(g)
        tg += g
    pat['gols'] = gol[:]
    pat['total'] = tg
    final.append(pat.copy())
    gol.clear()
    tg = 0
    s = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if s in 'N':
        break
    print('+'*30)
print(pat)
print(final)
print('-='*40)
print(f'{"Cod"}   {"Nome"}         {"Gols"}       {"Total"}')
for c in range(0, len(final)):
    t = final[c]
    g = str(t['gols'])
    print(f'{c:<3} {t["nome"]:<15} {g:<15}', end=' ')
    print(f'{t["total"]:<20}', end=' ')
    print()
while True:
    n = int(input('Mostrar dados de qual jogador(999 sair): '))
    if n != 999:
        if n <= len(final) - 1:
            print(f'{"<"*5}Levantamento do jogador {final[n]["nome"]}{">"*5}')
            for c in range(0 , len(final[n]['gols'])):
                print(f'No jogo {c} fez {final[n]["gols"][c]} gols')
        else:
            print('VALOR ERRADO, TENTE NOAVAMENTE')
    else:
        break
print('FIM')
for k, v in enumerate(final):
    print(f'{k:<3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()

