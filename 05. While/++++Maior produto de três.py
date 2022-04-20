def maior_produto3(lista):
    g = len(lista)
    a = 0
    b = 1
    c = 2
    produtomax = 0
    while a < g:
        b = 0
        while b < g:
            c = 0
            while c < g:
                if a != b and a != c and b != c:
                    produto = lista[a]*lista[b]*lista[c]
                    if produto > produtomax:
                        produtomax = produto
                c += 1
            b += 1
        a += 1
    return produtomax