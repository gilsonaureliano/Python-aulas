"""Digite uma, duas ou três letras e receba o retorno do número da coluna de acordo com o excel"""

alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
       's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

res = []
pag = []

per = str(input('Digite uma, duas ou três letras para retornar o número da coluna: ')).upper()
pos = ''
valor = ''
for c in range(0, len(alf)):
    al = alf[c]
    n1 = al.upper()
    res.append(n1)
for c in range(0, len(alf)):
    for c2 in range(0, len(alf)):
        al = (alf[c] + alf[c2])
        n1 = al.upper()
        res.append(n1)
for c in range(0, len(alf)):
    for c2 in range(0, len(alf)):
        for c3 in range(0, len(alf)):
            al = (alf[c] + alf[c2] + alf[c3])
            n1 = al.upper()
            res.append(n1)

for indice, v in enumerate(res):
    valor = v

    if valor == per:
        pos = indice + 1
        break

print(f'Você digitou a letra(s) \33[31m {per} \33[m e a coluna em Excel é a de número \33[31m {pos} \33[m')
