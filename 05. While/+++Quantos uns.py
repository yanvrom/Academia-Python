def quantos_uns(x):
    numerodeuns = 0
    while x > 0:
        resto = x % 10
        if resto == 1:
            numerodeuns += 1
        x = x // 10
    return numerodeuns