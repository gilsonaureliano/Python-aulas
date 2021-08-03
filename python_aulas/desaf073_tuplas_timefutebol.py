time = ('Flamento', 'Internacional', 'Atletico Mineiro', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
        'Atletico PR', 'Bragantino', 'Ceará', 'Corinthias', 'Atletico Goias', 'Bahia', 'Sport','Fortaleza',
        'Vasco', 'Goias', 'Coritiba', 'Botafogo')
print('O 5 primeiros colocados')
for c in range (0 ,5):
    print(f' {c + 1} colocado - {time[c]}')
print(time[:5])
print('+=' * 60)
print('Os ultimos 4 colocados')
for c in range (len(time)-4 , len(time)):
    print(time[c])
print(time[-4:])
print('+=' * 60)
print('Lista em Ordem Albetica')
print(sorted(time))
print('+=' * 60)
print('Qual a posição do Sport')

p = (time.index('Sport')) + 1
print(f'A Posição do Sport foi {p}')
