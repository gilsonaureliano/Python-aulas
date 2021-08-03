from urllib import request
try:
    a = 'http://pudim.com.br/'
    page = request.urlopen(a)
    print('PAGINA ENCONTRADA')
except:
    print('\033[41mERRRO')
