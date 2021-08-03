v = [] #ou list ()
for c in range(0, 5):
    v.append(int(input(f'Digite o valor da {c}ª posição: ')))
print(f'Você digitou a lista {v}')
print(f'O maior valor {max(v)} e estão na posição', end=' ')
for r in range(0, 5):
    if v[r] == max(v):
        print(f'{r}...', end=' ')
print(f'\nO menor valor {min(v)} está na posição', end=' ')
for p in range(0, 5):
    if v[p] == min(v):
        print(f'{p}...', end=" ")
