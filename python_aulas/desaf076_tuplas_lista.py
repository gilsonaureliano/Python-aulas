lista = ('Caderno', 25.30 , 'Caneta', 1.50, 'Borracha', 0.80, 'Livro', 68, 'Estojo', 7.30, 'Lapis', 1.75 , 'Mochila',
         120, 'Sapato', 98, 'Blusa', 45, 'Kit Desenho', 48.30 , 'Apagador', 3.60, 'Lapis Cera', 7.80)
print('='*60)
print('{:^60}'. format('LISTAGEM DE PREÇOS'))
print('='*60)
for c in range (0, len(lista), 2):
    preco = f'{lista[c + 1]:.2f}'
    print('{:.<50}R$ {: >7} '.format(lista[c],preco))
print('='*60)
