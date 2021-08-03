from random import sample, shuffle

al1 = input('Nome 1º aluno: ')
al2 = input('Nome 2º aluno: ')
al3 = input('Nome 3º aluno: ')
al4 = input('Nome 4º aluno: ')
print('Lista de Apresentação')
print(sample([al1, al2, al3, al4], k=4))

# outra forma de codificar
lista = [al1, al2, al3, al4]
shuffle(lista)
print(lista)
