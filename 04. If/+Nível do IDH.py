def nivel_idh(idh):
    if 0.800 <= idh <= 1000:
        return 'Muito Alto'
    if 0.700 <= idh < 0.800:
        return 'Alto'
    if 0.555 <= idh < 0.700:
        return 'Médio'
    if 0.350 <= idh < 0.555:
        return 'Baixo'
    if idh < 0.350:
        return 'Sem dados'