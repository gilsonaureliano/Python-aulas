n1 = float(input("Qual foi sua primeira nota: "))
n2 = float(input('Qual foi sua segunda nota: '))
media = (n1 + n2)/2

if media > 7:
    print('Sua media é {} e você está \033[7;32mAPROVADO\033[m'.format(media))
elif 5 < media <= 6.9:
    print('Sua media é {} e você está em \033[7;33mRECUPERAÇÃO\033[m')
else:
    print('Sua media é {} e você está \033[7;31mREPROVADO\033[m'.format(media))