n = 1
total = 0
zeroonze = 0
dozedeze = 0
dezoivintcin = 0
vinseistrincin = 0
trinseicinqnov = 0
sessentamais = 0
while n >= 0:
    n = int(input('Idade: '))
    if n < 0:
        continue
    elif n <= 11:
        zeroonze += 1
    elif n <= 17:
        dozedeze += 1
    elif n <= 25:
        dezoivintcin += 1
    elif n <= 35:
        vinseistrincin += 1
    elif n <= 59:
        trinseicinqnov += 1
    elif n >= 60:
        sessentamais += 1
    total += 1

print(f'0-11 anos: {(100*zeroonze/total):.2f} %')
print(f'12-17 anos: {(100*dozedeze/total):.2f} %')
print(f'18-25 anos: {(100*dezoivintcin/total):.2f} %')
print(f'26-35 anos: {(100*vinseistrincin/total):.2f} %')
print(f'36-59 anos: {(100*trinseicinqnov/total):.2f} %')
print(f'Acima de 60 anos: {(100*sessentamais/total):.2f}%')