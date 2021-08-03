num = [6, 9, 3, 8, 7]
print(num)
num.append(22)
print(num)
num.insert(2, 44)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
del num[0]
print(num)
num.pop()
print(num)
num.remove(9)
print(num)
print(f'{len(num)}')
if 7 in num:
    num.remove(7)
    print(num)
print('+'*60)
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for c , v in enumerate(valores):
    print(f'{c} posição ---  item: {v}')
v = list()
for cont in range(0,4):
    v.append(int(input('Digite o valor: ')))
print(v)
a = [1, 2, 3, 5]
b = a
b[2] = 8
print('+'*60)
print(a)
print(b)
print('+'*60)
a = [1, 2, 3, 5]
b = a[:]
b[2] = 8
print(a)
print(b)
