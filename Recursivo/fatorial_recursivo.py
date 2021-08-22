def fatorial (n):
    if n == 1:
        return 1
    else:
        valor = n * fatorial(n-1)
        return valor


res = fatorial(5)
print(res)