def posicoes_possiveis(mesa, pecas):
    listaposicoes = [] 
    if mesa == []:
        a = 0
        for i in pecas:
            listaposicoes.append(a)
            a+=1
    else:
        numerospossiveis = [mesa[0][0], mesa[len(mesa)-1][1]]
        i = 0
        for peca in pecas:
            if peca[0] in numerospossiveis or peca[1] in numerospossiveis:
                listaposicoes.append(i)
            i += 1
    return listaposicoes
