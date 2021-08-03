teste = list()
teste.append('Gilson')
teste.append(55)
print(teste)
galera = list()
galera.append(teste[:])
print(galera)
print('+='*20)
teste[0] = 'CIDA'
galera.append(teste[:])
print(galera)
print('+='*20)
galera = [['Pesro', 60], ['Cida', 40], ['Milena', 20]]
for c in galera:
    print(c[1])
    print(f' {c[0]} tem {c[1]} anos')
    