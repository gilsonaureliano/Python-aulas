p = str(input('EScreva uma frase: ')).lower()  # vai ler e dizer se lido normal e de traz para frente é igaul
palavras = p.split()
sem = ''.join(palavras)
print(sem)
l = p.replace(" ", "")  # reescreve trocando os espaços vazios por nada - uni as palavras
print(l)
n = len(l)
# print(n)
# print('++++++++')
for cnt in range (n -1 , -1, -1):
    # print('{}'.format(cnt) , end= ' ')
    print('{}'.format(l[cnt]), end= '') # para imprimir de traz para a frente
s = 0
for c in range(0, n):
    if l[c] == l[n - 1 - c]:
        s = s + 1

if s == n:
    print('\n A frase é Palíndromo')
else:
    print('\n Esta frase NÃO é Palíndromo')
