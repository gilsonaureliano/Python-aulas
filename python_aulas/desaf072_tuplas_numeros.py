num = ('Zero', 'Um', 'Dois', 'três', 'Quatro' , 'Cinco', 'Seis' , 'Sete' , 'Oito', 'Nove', 'Dez', 'Onze',  'Doze',
       'Treze', 'Quatorze', 'Quinze', 'Dezesseis' ,'dezesete' , 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if n < 0 or n > 20:
        print('Dado Invalido, temte novamente!', end=' ')
    else:
        print(f' Voce digitou o numero {n} - {num[n]}')
    r = str(input('Quer coninuar? [S/N]')).upper()
    if r == 'N':
        break


