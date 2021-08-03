import random

al1 = input('Nome 1º aluno: ')
al2 = input('Nome 2º aluno: ')
al3 = input('Nome 3º aluno: ')
al4 = input('Nome 4º aluno: ')

sort = random.choice([al1, al2, al3, al4])

# poderiamos colocar as opçes numa lista: lista = [al1, al2, al3, al4]

print('O aluno sorteado para limpar o quadro é: {}'.format(sort))
