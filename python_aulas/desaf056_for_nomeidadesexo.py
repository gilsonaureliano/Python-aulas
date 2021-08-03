hnome = ""
idm = 0
md = 0
tm = 0
for t in range(1, 5):
    print('='*5, '{}ª Pessoa'.format(t),'='*5)
    nome = str(input("Qual o seu nome: ")).upper()
    idd = int(input('Quantos anos você tem: '))
    sx = str(input('Qual o seu sexo [M] ou [F]: ')).upper()
    md = idd + md
    if idd > idm and sx == 'M':
        idm = idd
        hnome = nome
    if sx == 'F' and idd < 20:
        tm = tm + 1
media = md / 4
print(" ")
print('=' * 30)
print("""-> A media das idades é {} anos
-> O nome do homem mais velho é {} 
-> O total de mulheres abaixo de 20 anos é {}""".format(media, hnome, tm))
print('=' * 30)
