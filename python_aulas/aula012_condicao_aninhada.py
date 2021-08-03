nome = str(input('Escreva qual o seu nome: '))
if nome == 'gilson':
    print('\033[034m Que belo nome!')
elif nome == 'pedro' or nome == 'maria' or nome == 'cida':
    print('Você tem um nome normal')
elif nome in 'milena claudia judite marta':
    print('Que nome feminino lindo')
else:
    print('Tenha um bom dia {}{}'.format('\033[33m', nome))
