def nota_quizzes(q1, q2, q3, q4, q5):
    if q1<0 or q1>10:
        return 0
    if q2<0 or q2>10:
        return 0
    if q3<0 or q3>10:
        return 0
    if q4<0 or q4>10:
        return 0
    if q5<0 or q5>10:
        return 0
        
    notas = [q1, q2, q3, q4, q5]
    list.sort(notas)
    mediaquizes = (notas[1]+notas[2]+notas[3]+notas[4])/4
    return mediaquizes