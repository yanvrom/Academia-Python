def valida_cpf(a,b,c,d,e,f,g,h,i,j,k):
    if a==b==c==d==e==f==g==h==i==j==k:
        return False
    else:
        soma = (a*10 + b*9 + c*8 + d*7 + e*6 + f*5 + g*4 + h*3 + i*2)*10
        soma2 = (a*11 + b*10 + c*9 + d*8 + e*7 + f*6 + g*5 + h*4 + i*3 + j*2)*10
        resto = soma % 11
        resto2 = soma2 % 11
        if resto == 10:
            resto = 0
        if resto2 == 10:
            resto2 = 0
        if resto == j and resto2 == k:
            return True
        else:
            return False