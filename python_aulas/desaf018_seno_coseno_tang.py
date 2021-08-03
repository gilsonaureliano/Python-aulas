import math
# EX: 45° × π/180 = 0,7854rad

n1 = float(input("Digite um angulo: "))
angulo = math.radians(n1)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print("Seno de {:.0f}°Graus é {:.4f}" .format(n1, seno))
print('Cosseno de {:.0f}°Graus é {:.4f}'. format(n1, cosseno))
print('Tangente de {:.0f}°Graus é {:.4f}'.format(n1 , tangente))

