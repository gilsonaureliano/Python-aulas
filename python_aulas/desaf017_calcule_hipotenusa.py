import math #calcula a hipotenusa
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto adjacente: '))
h = math.hypot(co, ca)
print('A hipotenusa {:.2f} é o rsultato dos catetos {} e {}'.format(h, co, ca))

# outra forma

hip = (co**2 + ca ** 2)** (1/2)
print(hip)