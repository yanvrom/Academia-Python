velocidade = float(input('Qual a velocidade do automóvel em km/h? '))
if velocidade <= 80:
    print('Não foi multado')
else:
    multa = (velocidade - 80)*5
    multa = '%.2f' % (multa)
    print(multa)