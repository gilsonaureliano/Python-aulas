from datetime import date
sexo = str(input('Qual o seu sexo [M] ou [F]: '))
if sexo == 'M':
    nasc = int(input('informe o ano você nasceu: '))
    ano = date.today().year
    idade = ano - nasc
    print('No ano de {} você tem {} anos'.format(ano , idade))
    if idade > 18:
        print('sua idade é {} anos e\033[4;31m você já passou {} anos do prazo de alistamento \033[m'.format(idade, idade - 18))
        print('Seu ano de alistamento foi {} ' .format(nasc + 18))
    elif idade == 18:
        print('\033[32mVocê tem {}, Chegou a hora de seu alistamento\033[m'.format(idade))
    else:
        print('\033[7;35mSua idade é {} ano, aguarde {} anos para seu alistamento\033[m'.format(idade, 18 - idade))
        print('Você vai se alistar no ano {}'.format(ano + 18 - idade))
else:
    print(' Não Há Alistamento para mulheree, obrigado')