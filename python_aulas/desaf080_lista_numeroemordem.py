lista = list()
c = 0
while True:
    c += 1
    r = len(lista)
    n1 = (int(input('Digite um valor C: ')))
    if c == 1:
        lista.append(n1)
        print('Primeiro valor adicionado na lista...')
    else:
        if n1 > lista[c - 2]:
            lista.append(n1)
            print('Adicionado ao final da lista...')
    for d in range(0,r):
        if n1 < lista[d]:
            lista.insert(d , n1)
            print(f'Adicionado na posição {d} da lista')
            break
    if c == 5:
        print(f' Você digitou os numeros {lista}')
        break







