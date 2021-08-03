c = s = 0
while True:
    n = int(input('Digite um numero [999 sai do progrma]'))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} e total é {s}')
