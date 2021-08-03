pat = {}
gol = []
tg = 0
pat['nome'] = str(input('Nome do Jogador: '))
p = int(input('Quantas partidas jogou: '))
for c in range(0, p):
    g = int(input(f"Quantos gols na partida {c}: "))
    gol.append(g)
    tg += g
pat['gols'] = gol
pat['total'] = tg
print('-='*40)
for k, v in pat.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {pat["nome"]} jogou {p} partidas')
for c in range(0, len(gol)):
    print(f'{"=>":>10} Na partida {c}, fez {gol[c]} gols.')
print(f'Foi um total de {tg} gols')
