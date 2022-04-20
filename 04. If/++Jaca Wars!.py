import math
vel = float(input('Defina a velocidade inicial da jaca: '))
teta = float(input('Defina o ângulo inicial de lancamento: '))
d = (vel**2)*math.sin(math.radians(2*teta))/9.8

if 98 <= d <= 102:
    print('Acertou!')
elif d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')