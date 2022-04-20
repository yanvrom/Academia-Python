def classifica_triangulo(a,b,c):
    if a == b == c:
        return 'equilátero'
    else:
        if a==b or a==c or b==c:
            return 'isósceles'
        else:
            return 'escaleno'