import random


carteira = 100
while carteira != 0:
    sorteado = random.randint(0, 36)
    print(carteira)
    valorapostado = (input('Aposta:'))
    valorapostado = float(valorapostado)
    if valorapostado == 0:
        break
    aposta = input('Número ou paridade? (n/p) ')
    if aposta == 'n':
        numeroapostado = float(input('Escolha um valor de 0 a 36: '))
        if sorteado == numeroapostado:
            carteira += valorapostado*35
        if sorteado != numeroapostado:
            carteira -= valorapostado
    elif aposta == 'p':
        paridadeapostada = input('Par ou ímpar?(p/i)')
        if sorteado % 2 == 0 and paridadeapostada == 'p':
            carteira += valorapostado
        if sorteado % 2 == 1 and paridadeapostada == 'i':
            carteira += valorapostado
        if (sorteado %2 == 1 and paridadeapostada == 'p') or (sorteado%2 == 0 and paridadeapostada =='i'):
            carteira -= valorapostado
print(carteira)