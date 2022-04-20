def soma_multiplos(x, y):
    if x >= y:
        maximo = x*10
    elif y > x:
        maximo = y*10
    multiplox = 0
    multiploy = 0
    multiplos = []
    while multiplox <= (maximo - x):
        multiplox += x
        multiplos = multiplos + [multiplox]
    while multiploy <= (maximo -y):
        multiploy += y
        if multiploy not in multiplos:
            multiplos = multiplos + [multiploy]
    k = 0
    soma = 0
    while k < len(multiplos):
        soma += multiplos[k]
        k += 1
    return soma