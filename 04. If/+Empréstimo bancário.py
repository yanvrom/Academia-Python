def main():
    valor = int(input('Valor da casa: '))
    salario = int(input('Salário: '))
    anos = int(input('Quantidade de anos a pagar?'))
    meses = anos * 12
    prestacao = valor/meses
    if prestacao > (0.3*salario):
        print('Empréstimo não aprovado')
    else :
        print('Empréstimo aprovado')

main()