import math

def sen(x):
    senx = ((4*x)*(180 - x))/(40500 - x*(180 - x))
    return senx

angulo = 0
maiorerro = 0
b = 0
while angulo <= 90:
    erro = abs(sen(angulo) - math.sin(math.radians(angulo)))
    if erro > maiorerro:
        maiorerro = erro
        b = angulo
    angulo += 1

print(b)