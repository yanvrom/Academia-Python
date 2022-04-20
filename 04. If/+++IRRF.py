salbruto = float(input('Salário bruto: '))
dependentes = int(input('Número de Dependentes: '))

if salbruto <= 1045.00:
    aliquota = salbruto*7.5/100
elif salbruto <= 2089.60:
    aliquota = salbruto*9/100
elif salbruto <= 3134.40:
    aliquota = salbruto*12/100
elif salbruto <= 6101.06:
    aliquota = salbruto*14/100
if salbruto > 6101.06:
    aliquota = 671.12

inss = aliquota

basedecalculo = salbruto - inss - dependentes*189.59

if basedecalculo <= 1903.98:
    aliquota2 = 0
    deducao = 0
elif basedecalculo <= 2826.65:
    aliquota2 = 7.5/100
    deducao = 142.80
elif basedecalculo <= 3751.05:
    aliquota2 = 15/100
    deducao = 354.80
elif basedecalculo <= 4664.68:
    aliquota2 = 22.5/100
    deducao = 636.13
if basedecalculo > 4664.68:
    aliquota2 = 27.5/100
    deducao = 869.36

irrf = basedecalculo*aliquota2 - deducao

print(irrf)
