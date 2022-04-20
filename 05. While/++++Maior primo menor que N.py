def maior_primo_menor_que(x):
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
    if x <= 1:
        return -1
    while x >= 2:
        if verifica_primo(x):
            return x
        x -= 1