def verifica_idade(idade):
    if idade < 18 :
        return 'Não está liberado'
    else :
        if idade >= 18 and idade <21:
            return 'Liberado BRASIL'
        else:
            return 'Liberado EUA e BRASIL'