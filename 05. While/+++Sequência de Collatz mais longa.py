def numero_de_termos(x):
    numerodetermos = 1
    n = x
    while n != 1:
        if n % 2 == 1:
            n = 3*n + 1
        elif n % 2 == 0:
            n = n/2
        numerodetermos += 1
    return numerodetermos
maximo = 0
a = 1
while a < 1000:
    k = numero_de_termos(a)
    if k > maximo:
        maximo = k
        numeromax = a
    a += 1
    
print(numeromax)