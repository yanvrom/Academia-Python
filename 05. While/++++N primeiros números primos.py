def lista_primos(n):
    def verifica_primo(x):
        i = 2
        if x == 0 or x == 1:
            return False
        if x == 2:
            return True
        while i <= x/2:
            if x % i == 0:
                return False
            i +=1
        return True
    lista = []
    i = 2
    while len(lista) < n:
        if verifica_primo(i):
            lista.append(i)
        i += 1
    return lista