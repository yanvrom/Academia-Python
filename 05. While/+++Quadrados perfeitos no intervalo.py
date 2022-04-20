from math import floor
def quadrados_no_intervalo(a, b):
    if a <= b:
        x = a
        y = b
    elif a > b:
        x = b
        y = a 
    quadrados = 0
    while x <= y:
        raiz = x**(1/2)
        raizinteira = floor(raiz)
        if raiz == raizinteira:
            quadrados += 1
        x += 1
    return quadrados