def maximo_divisor_comum(x, y):
    n = 2
    maxdiv = 1
    while n <= x and n <= y:
        if x % n == 0 and y % n == 0:
            x = x / n
            y = y / n
            maxdiv = maxdiv*n
            if x % n == 0 and y % n == 0:
                continue
        n = n + 1
    return maxdiv
            