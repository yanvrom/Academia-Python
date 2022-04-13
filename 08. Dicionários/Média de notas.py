def calcula_media(listadenotas):
    somanotas = 0
    total = 0
    for dicionario in listadenotas:
        for nota in dicionario.values():
            somanotas += nota
            total += 1
    return somanotas/total