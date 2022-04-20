def pacotes_correio(pacotes):
    numeropacotes = len(pacotes)
    k = 0
    if (pacotes[0])[0] != numeropacotes:
        return "pacote perdido"
    while k < numeropacotes:
        if (pacotes[k])[1] != k+1:
            return 'ordem errada'
        k += 1
    k = 1
    while k < (numeropacotes - 1):
        if (pacotes[k])[2] != (pacotes[0][2]):
            return 'tamanho errado'
        k += 1
    return 'tudo certo'