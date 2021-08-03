palavras = ('Casa', 'viaduto', 'castelo', 'Martelo', 'Estrada', 'Viagem', 'Petroleo', 'Apartamento')
for c in range(0 , len(palavras)):
    n = palavras[c]
    g = str.lower(n)
    f = str.upper(n)
    print('\nA palavra {} possui as vogais: '.format(f), end=' ')
    for d in range(0, len(n)):
        if n[d] in 'AaEeIiOoUu':
            print('{}'.format(g[d]), end=' ')
