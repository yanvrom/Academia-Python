def maior_fator_primo(x):
    maior_fator = 2
    while x % 2 == 0:
        x = x / 2
    while x != 1:
        if maior_fator == 2:
            maior_fator = 3
        while x % maior_fator == 0:
            x = x / maior_fator
        maior_fator += 2
    return maior_fator - 2