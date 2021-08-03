c = ' '
ct = 0
sm = 0
maiorv = 0
menorv = 0
while c not in 'N':
    v = float(input('Digite uma valor: '))
    ct = ct + 1
    sm = sm + v
    if ct == 1:
        maiorv = v
        menorv = v
    else:
        if v > maiorv:
            maiorv = v
        if v < menorv:
            menorv = v
    c = str(input('Deseja continuar [S/N]: ')).upper()
media = sm / ct
print("""Foram digitados {} vezes
Soma igual {}
Média {:.2}
Maior {}
menor {}""".format(ct, sm, media, maiorv, menorv))
