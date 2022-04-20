def PiWallis(n):
    pi = 1
    x = 1
    while x <= n:
        if x % 2 == 0:
            pi = pi*x/(x+1)
        if x % 2 == 1:
            pi = pi*(x+1)/x
        x += 1
    return 2*pi