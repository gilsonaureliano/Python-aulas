frase = 'Curso em video Python'
print(frase)
print(frase[3])  # a resposta será s
print(frase[3:13])
print(frase[:13])  # do inicio até a posição 12 serão mostradas
print(frase[13:])  # do 13 ate o final
print(frase[1:13])
print(frase[1:13:2])  # pulando de 2 em 2
print(frase.count('o'))  # aqui o programa considera maiuscula e minuscula
print(frase.upper().count('O'))  # transforma tudo em maiuscula e conta o O maisusculo
print(len(frase))  # mostra o tamanho
print(frase.replace('Python', 'Android'))  # assim não salva na variavel a troca
frase = (frase.replace('Python', "TROCANDO"))
print(frase)
print(len(frase))  # mostra o tamanho
print('Curso' in frase)
print(frase.find('video'))
print(frase.find('Video'))  # mudei o V para maiuscula , nao tem a palavra, resulato -1
print(frase.split())
dividivo = (frase.split())  # criou uma lista dentro da variavel dividivo
print(dividivo)
print(dividivo[0])  # mostra o texto na posição zero da lista
print(dividivo[0][3])  # mostra o texto na posição zero da lista e a terceira letra

print("""hfhfhfjfjfjfjfjjfj
yyyyyyyyyyyyyyyyyy
jjjjjjjjjjjjjjjjjj
kkkkkkkkkkkkkkkkk""")
