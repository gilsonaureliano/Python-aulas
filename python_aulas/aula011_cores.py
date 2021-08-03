print('\033[1;33;44m Olá Mundo \033[m')
print(' ')
print('\033[7;33;44m Olá Mundo \033[m')
print(' ')
a = 3
b = 5
print('Os valores \033[35m{}\033[m e \033[31m{}\033[m !!!!!'. format(a ,b))
nome = 'Gilson'
print('Olá,  {}{}{}.!!!!!'.format('\033[1;33m',nome ,'\033[m'))

cores = {'limpa':'\033[m' , 'azul': '\033[34m'}
print('Olá,  {}{}{}.!!!!!'.format(cores['azul'] , nome , cores['limpa']))

