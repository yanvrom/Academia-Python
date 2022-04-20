def divisivel(x):
    if x % 2 == 0 and x % 3 == 0:
        return 'Insper'
    else:
        if x % 2 == 0:
            return 'Ins'
        if x % 3 == 0:
            return 'per'
        else:
            return x