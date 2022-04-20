def calcula_investimento(investini, meses, nome):
    tempo = 1
    valor = investini
    if nome == 'CDB':
        while tempo <= meses:
            valor = valor*1.013
            if tempo % 6 == 0:
                valor = valor*1.012
            tempo += 1
    if nome == 'LCI':
        while tempo <= meses:
            valor = valor*1.016
            tempo += 1
    if nome == 'LCA':
        while tempo <= meses:
            valor = valor*1.0145
            if tempo % 4 == 0:
                valor = valor*1.01
            tempo += 1
    return valor