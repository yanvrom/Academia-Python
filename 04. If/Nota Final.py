def nota_final(mediaquizes, ai, af, ep1, ep2, pf):
    if mediaquizes<0 or mediaquizes>10:
        return 0
    if ai<0 or ai>10:
        return 0
    if af<0 or af>10:
        return 0
    if ep1<0 or ep1>10:
        return 0
    if ep2<0 or ep2>10:
        return 0
    if pf<0 or pf>10:
        return 0

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
        