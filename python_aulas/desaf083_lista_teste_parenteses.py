p = str(input('Digite uma expressão matematica com (): '))
ct = m = 0
for c in range(0, len(p)):
    if p[c] in '(':
        ct += 1
print(ct)
for t in range(0, len(p)):
    if p[t] in ')':
        m += 1
if ct == m:
    print('Expressão é valida')
else:
    print('Expressão Invalida')

print('+'*100)

f = list ()
a = str(input('Expressão: '))
for c in range(0 , len(a)):
    f.append(a[c])
if f.count('(') == f.count(')'):
    print('Expressão Valida')
else:
    print('Deu merda')


