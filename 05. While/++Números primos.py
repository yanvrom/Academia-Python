def eh_primo(x):
    k = 2
    if x == 0 or x == 1:
        return False
    while k < (x/2 + 1):
        if x % k == 0:
            return False
        k += 1
    return True