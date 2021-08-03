from datetime import date
ano = int(input('Digite um ano qualquer - Caso deseje o ano atual digite 0 : '))
if ano == 0:
   ano = date.today().year # pega o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano: {} é bissexto'.format(ano))
else:
     print('{} não é bissexto'.format(ano))
