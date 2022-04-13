def classifica_idade(idade):
    if idade <= 11:
        return 'crianca'
    if 11 < idade <= 17:
        return 'adolescente'
    if 17 < idade:
        return 'adulto'