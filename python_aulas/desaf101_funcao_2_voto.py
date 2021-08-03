def voto(n):
    from datetime import date
    global ano
    ano = date.today().year - n
    if 65 > ano >= 18:
        r = 'OBRIGATÓRIO'
        return r
    if ano < 18:
        r = 'NEGADO'
        return r
    if ano > 65:
        r = 'OPCIONAL'
        return r


# programa principal

print('-=' * 20)
ano = int(input('Ano de nascimento: '))
r = voto(ano)
print(f'Com {ano} anos seu voto é {r}')
