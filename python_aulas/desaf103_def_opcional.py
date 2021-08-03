def ficha(a='DESCONHECIDO',  b=0):
    print(f'O jogador {a} fez {b} gols')


# programa principal
nome = str(input('Nome do Jogador: '))
gol = str(input('Numero de gols: '))
if str.isalpha(nome) and str.isnumeric(gol):
    gol = int(gol)
    ficha(nome, gol)
elif not str.isalpha(nome) and str.isnumeric(gol):
    gol = int(gol)
    ficha(b=gol)
elif str.isalpha(nome) and not str.isnumeric(gol):
    ficha(a=nome)
else:
    ficha()
