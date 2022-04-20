def decimal_para_binario(x):
    if x < 0:
        return "Negativo"
    quociente = 1
    numeroinv = []
    while quociente != 0:
        quociente = x // 2
        resto = x % 2
        x = quociente
        numeroinv.append(resto)
    y = len(numeroinv)
    numero = ''
    while y >=1:
        numero = f'{numero}{numeroinv[y-1]}'
        y -= 1
    return numero
