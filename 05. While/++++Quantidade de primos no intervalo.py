def primos_entre(a,b):
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
    quantidade = 0
    aux = a
    while aux <= b:
        if verifica_primo(aux):
            quantidade += 1
        aux += 1
    return quantidade