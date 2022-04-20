def valida_data(dia,mes,ano):
    if ano % 4 == 0 and ano % 400 == 0 and mes == 2:
        if 1 <= dia <= 29:
            return True
        else:
                return False
    elif mes == 2:
        if 1 <= dia <= 28:
            return True
        else:
            return False

    if mes < 1 or mes > 12:
        return False
    meses31 = [1, 3, 5, 7, 8, 10, 12]
    meses30 = [4, 6, 9, 11]
    if mes in meses31:
        if 1 <= dia <= 31:
            return True
        else:
            return False
    elif mes in meses30:
        if 1 <= dia <=30:
            return True
        else:
            return False