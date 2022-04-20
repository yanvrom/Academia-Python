import random

def apostando_em_dados(numsorte, valor, numrodadas):
    rodada = 1
    while rodada <= numrodadas:
        numsorteado = random.randint(1, 6)
        if numsorte == numsorteado:
            valor = 4*valor/3
        else:
            valor = 5*valor/6
        rodada += 1
    return valor