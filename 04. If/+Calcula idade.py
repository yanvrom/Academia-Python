def calcula_idade(dia,mes,ano,dia2,mes2,ano2):
    x = ano2 - ano
    if mes2 < mes:
        return x - 1
    if mes2 > mes:
        return x
    if mes2 == mes:
        if dia2 >= dia:
            return x
        else:
            return x - 1