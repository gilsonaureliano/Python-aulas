while True:
    tabuada = int(input('Qual o valor da tabuada: '))
    if tabuada < 0:
        break
    print('+' * 15)
    for c in range(0, 10):
        c += 1
        print(f'{tabuada} x {c} = {tabuada * c}')
    print('+' * 15)
print('ACABOU')
