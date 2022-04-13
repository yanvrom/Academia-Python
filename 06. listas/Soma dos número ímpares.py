def soma_impares(numeros):
    soma = 0
    for i in range(len(numeros)):
        if numeros[i] % 2 == 1:
            soma += numeros[i]
    return soma