def aproxima_raiz(n):
    i = 1
    while i**2 < n:
        i = i + 1
    a = (i**2 - n)
    b = n - (i-1)**2
    if a > b:
        return i - 1
    elif b > a:
        return i