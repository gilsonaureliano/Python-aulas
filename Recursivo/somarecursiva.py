def somar(n):
    if len(n) == 1:
        return n[0]

    else:
        resp = n[0] + somar(n[1:])
        return resp


s = [2, 18, 25, 5, 10, -20]
res = somar(s)
print(res)


