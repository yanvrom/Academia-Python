def nota_quizzes(q1, q2, q3, q4, q5):
    notas = [q1, q2, q3, q4, q5]
    u = 0
    while u < 5:
        if notas[u] < 0 or notas[u]>10:
            return 0
        u += 1
    list.sort(notas)
    mediaquizes = (notas[1]+notas[2]+notas[3]+notas[4])/4
    return mediaquizes
    
def nota_final(mediaquizes, ai, af, ep1, ep2, pf):
    todasasnotas = [mediaquizes, ai, af, ep1, ep2, pf]
    p = 0
    while p < 6:
        if todasasnotas[p] > 10 or todasasnotas[p] < 0:
            return 0
        p+= 1
    Ni = 0.4*ai + 0.5*af + 0.1*mediaquizes
    Ng = 0.1*ep1 + 0.2*ep2 + 0.7*pf
    if Ni >= 5 and Ng>=5:
        Nf = (Ni + Ng)/2
    elif Ni < 5 or Ng < 5:
        if Ni < Ng:
            Nf = Ni
        elif Ng <= Ni:
            Nf = Ng
    return Nf

notas = []
resposta = input('Deseja adicionar as notas de mais um aluno? ')

while resposta != 'não':
    q1 = float(input('Nota do quiz 1 : '))
    q2 = float(input('Nota do quiz 2 : '))
    q3 = float(input('Nota do quiz 3 : '))
    q4 = float(input('Nota do quiz 4 : '))
    q5 = float(input('Nota do quiz 5 : '))
    notaquizes = nota_quizzes(q1,q2,q3,q4,q5)
    notaai = float(input('Nota da Ai: '))
    notaaf = float(input('Nota da Af: '))
    notaep1 = float(input('Nota do EP1: '))
    notaep2 = float(input("Nota do EP2: "))
    notaprojetofinal = float(input("Nota do Projeto Final: "))
    notafinalaluno = nota_final(notaquizes, notaai, notaaf, notaep1, notaep2, notaprojetofinal)
    print(f'Nota final do aluno: {notafinalaluno:.2f}')
    notas.append(notafinalaluno)
    resposta = input('Deseja adicionar as notas de mais um aluno? ')
if len(notas) != 0:
    mediasala = sum(notas)/(len(notas))
    print(f'Média da sala: {mediasala:.2f}')
elif len(notas) == 0:
    print(f'Média da sala: 0.00')
    print('Aprovados: 0.00%')
    print('Reprovados: 0.00%')
n = 0
aprovados = 0
reprovados = 0
while n < len(notas):
    if notas[n] >= 5:
        aprovados += 1
    elif notas[n] < 5:
        reprovados += 1
    n += 1
if len(notas) != 0:
    print(f'Aprovados: {100*aprovados/len(notas):.2f}%')
    print(f'Reprovados: {100*reprovados/len(notas):.2f}%')