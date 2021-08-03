p = float(input('Qual o seu peso kg: '))
a = float(input('Qual a sua altura M: '))
imc = p / a ** 2
print('Seu IMC é {}{:.1f}{}'.format('\033[33m', imc, '\033[m'))
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Seu peso é ideal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso')
elif 30 <= imc < 40:
    print('Você está com obesidade')
else:
    print('Sua Obsidade é mórbida')
    print('CUIDE DA SAUDE')

