lista = list()

while True:
    n = (int(input("Digite um numero: ")))
    if n in lista:
        print('Valor duplicado! Não adicionado...')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso!!!')
    while True:
        s = str(input('Quer continuar [S/N]')).upper().strip()
        if s not in 'SN':
            print('Resposta incorreta, tente novamente...')
        else:
            break
    if s in 'N':
        break
print(f'Você digitou os valores: {sorted(lista)}')