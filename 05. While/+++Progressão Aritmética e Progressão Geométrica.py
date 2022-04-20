def verifica_pa(lista):
    n = len(lista) - 1
    k = lista[1] - lista[0]
    while n >= 1:
        if lista[n] - lista[n-1] != k:
            return False
        n -= 1
    return True

def verifica_pg(lista):
    n = len(lista) - 1
    if 0 in lista:
        while n >= 0:
            if lista[n] != 0:
                return False
            n -= 1
        return True
    q = lista[1]/lista[0]
    while n >= 1:
        if lista[n]/lista[n-1] != q:
            return False
        n -= 1
    return True
        
    

def verifica_progressao(lista):
    if verifica_pa(lista) and verifica_pg(lista):
        return 'AG'
    elif verifica_pa(lista):
        return 'PA'
    elif verifica_pg(lista):
        return 'PG'
    else:
        return 'NA'